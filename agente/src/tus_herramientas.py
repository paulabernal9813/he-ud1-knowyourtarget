"""Herramientas iniciales de reconocimiento. AQUÍ PUEDES AÑADIR LAS TUYAS.

WHOIS (whois.py), DNS y crt.sh ya están implementadas y activas en lanzar.py.
DNS y crt.sh proceden de la solución del profesor (herramientas/recon.py).

Para ampliar: una tarea por función, @protegida, sin shell, con timeout,
salida recortada, errores como texto y resultados filtrados por el alcance.
Importa tu nueva función en lanzar.py y añádela a HERRAMIENTAS.

Ideas: subdominios_subfinder, wayback_urls, correos (theHarvester / hunter.io),
infraestructura_ip, correo_postura (SPF/DMARC/MTA-STS/CAA), urlscan, shodan_host.
"""

import json
import subprocess
import urllib.parse
import urllib.request
import requests

from guard import protegida, filtrar
from whois import recortar

UA = "aap-recon/1.0 (educativo; IES Rafael Alberti)"
TIPOS_DNS = {"A", "AAAA", "MX", "NS", "TXT", "CNAME", "SOA"}


def _http(url: str, timeout: int = 30) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", "replace")


@protegida(objetivo="dominio")
def dns_registros(dominio: str, tipo: str = "A") -> str:
    """Consulta registros DNS de un dominio. tipo: A, AAAA, MX, NS, TXT, CNAME o SOA.
    Devuelve los valores, uno por línea."""
    tipo = tipo.upper()
    if tipo not in TIPOS_DNS:
        return f"ERROR: tipo DNS no válido ({tipo}). Usa uno de: {', '.join(sorted(TIPOS_DNS))}."
    try:
        r = subprocess.run(["dig", "+short", tipo, dominio],
                           capture_output=True, text=True, timeout=20)
    except subprocess.TimeoutExpired:
        return "ERROR: dig no respondió en 20 segundos."
    except OSError as e:
        return recortar(f"ERROR: no se pudo ejecutar dig: {e}")
    if r.returncode != 0:
        return recortar(f"ERROR: dig falló ({r.returncode}): {r.stderr.strip() or 'sin detalles'}")
    salida = recortar(r.stdout.strip())
    return salida or f"Sin registros {tipo} para {dominio}."


@protegida(objetivo="dominio")
def subdominios_crtsh(dominio: str) -> str:
    """Enumera subdominios de un dominio por transparencia de certificados (crt.sh).
    Pasivo: no toca el objetivo. Devuelve solo los subdominios dentro del alcance."""
    url = f"https://crt.sh/?q=%25.{urllib.parse.quote(dominio)}&output=json"
    try:
        datos = json.loads(_http(url, timeout=90))
    except Exception as e:
        return (f"ERROR: crt.sh no respondió ({e}). crt.sh suele ir lento; "
                "puedes reintentar más tarde o añadir otra fuente de subdominios.")
    if not isinstance(datos, list) or any(
        not isinstance(fila, dict) or not isinstance(fila.get("name_value"), str)
        for fila in datos
    ):
        return "ERROR: crt.sh devolvió un formato de certificados inesperado."
    nombres = set()
    for fila in datos:
        for n in str(fila.get("name_value", "")).splitlines():
            n = n.strip().lstrip("*.").lower()
            if n:
                nombres.add(n)
    dentro, fuera = filtrar(sorted(nombres))
    cab = f"{len(dentro)} subdominios en alcance ({fuera} filtrados por estar fuera):\n"
    return recortar(cab + "\n".join(dentro))

import re
import urllib.error


class _SinRedireccion(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):
        return None


def _get_en_alcance(url: str, max_redir: int = 3):
    """GET que sigue redirecciones a mano, solo si cada destino está en alcance.
    Devuelve (url_final, texto) o (None, mensaje_de_error)."""
    opener = urllib.request.build_opener(_SinRedireccion)
    for _ in range(max_redir + 1):
        host = urllib.parse.urlparse(url).hostname or ""
        dentro, _fuera = filtrar([host])
        if not dentro:
            return None, f"BLOQUEADO: {host} está fuera de alcance"
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        try:
            with opener.open(req, timeout=10) as r:
                return url, r.read(200_000).decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            loc = e.headers.get("Location")
            if e.code in (301, 302, 303, 307, 308) and loc:
                url = urllib.parse.urljoin(url, loc)
                continue
            return None, f"HTTP {e.code}"
        except Exception as e:
            return None, f"ERROR: {e}"
    return None, "ERROR: demasiadas redirecciones"


@protegida(objetivo="dominio")
def analizar_robots_sitemap(dominio: str) -> str:
    """Lee robots.txt y los sitemaps del dominio (pasivo, pocas peticiones).
    Sigue redirecciones solo dentro del alcance y devuelve rutas y URLs en alcance."""
    host = dominio.replace("https://", "").replace("http://", "").split("/")[0]
    partes = []

    url_robots, texto = _get_en_alcance(f"https://{host}/robots.txt")
    sitemaps = []
    if url_robots is None:
        partes.append(f"=== robots.txt de {host} ===\n{texto}")
    else:
        lineas = [l.strip() for l in texto.splitlines()
                  if l.lower().startswith(("disallow", "allow", "sitemap"))]
        sitemaps = [l.split(":", 1)[1].strip() for l in lineas
                    if l.lower().startswith("sitemap")]
        partes.append(f"=== {url_robots} ===\n" + "\n".join(lineas[:60]))

    if not sitemaps:
        sitemaps = [f"https://{host}/sitemap.xml"]

    for sm in sitemaps[:3]:
        url_sm, texto = _get_en_alcance(sm)
        if url_sm is None:
            partes.append(f"=== {sm} ===\n{texto}")
            continue
        urls = re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", texto)
        en_alc = [u for u in urls
                  if filtrar([urllib.parse.urlparse(u).hostname or ""])[0]]
        partes.append(f"=== {url_sm} ===\n{len(en_alc)} URLs en alcance "
                      f"({len(urls) - len(en_alc)} fuera, filtradas). Primeras:\n"
                      + "\n".join(en_alc[:40]))
    return recortar("\n\n".join(partes))
