# Mapa de reconocimiento: SHEIN (*.shein.com)

Fecha: 2026-11-07 · Fase: reconocimiento pasivo (todavía no he tocado nada de forma activa) · Programa: SHEIN Security Response

## Cómo se leen las referencias

Al lado de cada dato pongo entre corchetes de dónde lo he sacado, para poder comprobarlo en mi cuaderno (`cuaderno.md`) o en el alcance (`scope.txt`):

| Ref. | De dónde sale |
| --- | --- |
| E0 | Fichero security.txt (no tiene hora) |
| E1 | 2026-11-03 16:45 · whois |
| E2 | 2026-11-03 16:50 · dig (NS, MX, TXT) |
| E3 | 2026-11-03 16:53 · subfinder (lista de subdominios) |
| E4 | 2026-11-03 21:25 · ficha de infraestructura (IP, servidor de nombres, hosting, tecnologías) |
| E5 | 2026-11-03 21:30 · robots.txt |
| E6 | 2026-11-03 21:40 · Shodan InternetDB |
| E7 | 2026-11-03 21:43 · búsqueda `filetype:pdf` |
| E8 | 2026-11-03 21:43 · búsqueda `intitle:"index of"` |
| E9 | 2026-11-03 21:50 · theHarvester |
| S | scope.txt (consultado el 1/11/2026) |

Regla que me he puesto: si algo no está en el cuaderno, no lo afirmo. Cuando me falta un dato lo digo claramente ("no obtenido").

---

## 1. Resumen

- SHEIN es una tienda online de ropa y más cosas. Por los subdominios (us, es, de, fr, jp, br...) parece que tiene una tienda distinta para cada país [E3].
- El alcance del programa es `*.shein.com`, pero `security.shein.com` está **fuera**. También quedan fuera otros dominios como shein.in, shein.tw o romwe.com [S].
- La web principal `shein.com` apunta a la IP 52.39.206.44, que está en AWS (Amazon), en el centro de datos de Oregón. El DNS lo lleva Route 53 y el dominio está registrado en hichina.com [E4].
- Según Shodan, esa IP solo tiene abiertos los puertos 80 y 443 (web), usa OpenResty/nginx y no tiene vulnerabilidades registradas [E6].
- Lo más llamativo: hay una cantidad enorme de subdominios, y algunos tienen pinta de ser de pruebas o internos (`bankltd-test01`, `privatelift`), además de VPNs y APIs [E3]. Todo esto es solo por el nombre; aún no he comprobado nada.

---

## 2. Dominios y subdominios

Solo tengo la IP de `shein.com` [E4]. De los demás subdominios solo tengo el nombre, que salió de subfinder [E3], así que en la columna de IP pongo "no resuelta" (todavía no la he consultado).

La columna "Para qué parece servir" es **una suposición mía a partir del nombre**, no algo que haya comprobado.

En alcance: todo lo que sea `*.shein.com` es **sí**, menos `security.shein.com`, que es **no** [S].

| Subdominio(s) | IP | En alcance | Para qué parece servir | Ref. |
| --- | --- | --- | --- | --- |
| `shein.com` (la raíz) | 52.39.206.44 | Sí | Web principal | E4, E6 |
| `www`, `m` | no resuelta | Sí | Web principal y versión móvil | E3 |
| `us`, `es`, `de`, `fr`, `it`, `nl`, `pl`, `pt`, `ro`, `se`, `ch`, `at`, `au`, `nz`, `sg`, `th`, `id`, `ph`, `kr`, `jp`, `tr`, `il`, `ru`, `za`, `ma`, `jo`, `br`, `ar`, `arg`, `cl`, `co`, `pe`, `ec`, `ca`, `roe`, `eur`, `asia` | no resuelta | Sí | Tiendas por país o región | E3 |
| `vn`, `in` | no resuelta | Sí (están bajo `*.shein.com`, aunque shein.in y shein.com.vn estén excluidos; ver duda en el apartado final) | Tiendas de Vietnam e India. Salen en Shodan, no en subfinder | E6, S |
| `api-gateway-central-dc`, `api-service`, `api-shein`, `api-cmc`, `gateway`, `static.gateway`, `callback-api` | no resuelta | Sí | APIs y gateways (la parte de "detrás" de la web y la app) | E3 |
| `im-api-chat-us/eur/central`, `im-gateway-chat-us/eur/central` | no resuelta | Sí | Chat o mensajería, repartido por regiones | E3 |
| `api-sensors`, `origin-api-sensors`, `analytics`, `www.analytics`, `count`, `cinfo-v4`, `cinfo-v6` | no resuelta | Sí | Analítica y estadísticas | E3 |
| `vpn`, `euvpn`, `usvpn`, `www.euvpn`, `www.usvpn`, `euqs` | no resuelta | Sí | Acceso por VPN (Europa y EE. UU.). De `euqs` no sé qué es | E3 |
| `bankltd-test01`, `www.bankltd-test01`, `privatelift`, `playback`, `www.playback`, `ipp`, `ccc-store` | no resuelta | Sí | Parecen de pruebas o internos (por "test" y "private"). No sé la función exacta | E3 |
| `seller-us`, `seller-eu`, `seller-br`, `partner.seller-us`, `case-studies.seller-us`, `events.seller-us`, `webinars.seller-us`, `articles.seller-us`, `blog.seller-us` | no resuelta | Sí | Portal para vendedores y partners, con su contenido | E3 |
| `marketplace`, `shop`, `exchange`, `eur-exchange-webview`, `app`, `onelink`, `preferences`, `service`, `info` | no resuelta | Sí | Marketplace, cambios o devoluciones, enlaces a la app, preferencias de cuenta, atención | E3 |
| `help`, `us.help`, `mus.help` | no resuelta | Sí | Centro de ayuda | E3 |
| `careers`, `jobs.careers`, `www.jobs.careers` | no resuelta | Sí | Empleo | E3 |
| `link`, `link2`, `link-<país>`, `link-<país>-new`, `link-news`, `link-news-new`, `link-email`, `link-emailmarket`, `link-market-us`, `link.edm`, `link.emaila` y las versiones con `www.` | no resuelta | Sí | Enlaces de redirección y seguimiento de campañas de correo | E3 |
| `tracking.news.*`, `tracking-us.news.*`, `tracking.mail.market*`, `edm`, `emailmarket`, `image.email` | no resuelta | Sí | Seguimiento y envío de email marketing | E3 |
| `cn3-mt168/169/180/181/182/183.notice`, `cn3-mt190.info-de` | no resuelta | Sí | Servidores de notificaciones o correo (creo que "mt" es *mail transfer*, pero es una suposición) | E3 |
| `img`, `img-eur`, `img-se`, `img-ru`, `image`, `image-tw/ca/mx/il/it`, `image.nl`, `imag2`, `s1` | no resuelta | Sí | Imágenes y archivos estáticos | E3 |
| `security.shein.com` | no resuelta | **No** | Excluido expresamente por el programa | E3, S |

**Cosa rara que he visto:** hay muchos hosts con `www.` delante de nombres que no deberían ser una web (por ejemplo `www.api-gateway-central-dc` o `www.link-it-new`). Puede ser que el DNS tenga un comodín (*wildcard*) y por eso todo "existe". Tengo que comprobarlo antes de fiarme de la lista [E3].

---

## 3. Infraestructura y servicios

**Hosting y DNS** [E4]
- IPv4 de `shein.com`: 52.39.206.44, en Amazon US West (Oregón).
- Servidor de nombres: `ns-893.awsdns-47.net` (AWS Route 53).
- Registrador del dominio: hichina.com.
- Cloud: AWS EC2 (máquinas virtuales de Amazon). Red: Route 53 (el servicio de DNS de Amazon).

**Tecnologías detectadas** [E4]: SSL (cifrado de la conexión) y, en el navegador, JavaScript asíncrono, Session Storage y Local Storage.

**Shodan InternetDB (IP 52.39.206.44)** [E6]
- Puertos abiertos: 80 y 443.
- Software: `openresty` y `nginx`.
- Nombres asociados a la IP: `shein.com`, `vn.shein.com`, `in.shein.com` y `ec2-52-39-206-44.us-west-2.compute.amazonaws.com`.
- Etiqueta: `cloud`. Vulnerabilidades: ninguna indexada.
- Al pedir `security.txt` y `robots.txt` me contestó un `301 Moved Permanently` de OpenResty, lo que encaja con lo de Shodan [E0, E5]. **Ojo, un fallo mío:** escribí `https:/shein.com` con una sola barra, así que ese 301 puede ser por el error y no por la web. Hay que repetirlo bien.

**Correo y verificaciones (registros TXT)** [E2]
- SPF: `v=spf1 include:safe-spf01.shein.com include:trustpilotservice.com include:spf-cm.icoremail.net ~all`. Dice qué servidores pueden mandar correo en nombre del dominio. Termina en `~all` (*softfail*), que es más permisivo que `-all`. Autoriza a Trustpilot y a icoremail.net.
- Hay verificaciones de varios servicios: Microsoft (`MS=`, tres), Google (varias), Figma (dos), Apple, Cursor, Cloudflare (`cloudflare_dashboard_sso`) y KnowBe4 (formación de concienciación en seguridad).
- **Problema:** pedí `NS MX TXT` en el mismo `dig`, pero solo salieron los TXT (avisó de "extra type option"). **No tengo los registros MX ni NS** [E2].
- Mi interpretación (a confirmar): parece que usan Microsoft 365 y/o Google Workspace, Cloudflare y herramientas de terceros. Con el MX lo sabría seguro.

**Lo que no he podido obtener**
- `whois`: "Network is unreachable", sin datos de registro [E1].
- Búsquedas en Google: `filetype:pdf` no dio nada [E7]. `intitle:"index of"` dio unas 20 páginas, pero cada una pedía CAPTCHA y siempre me daba "verificación fallida", así que no pude mirar el contenido [E8].

---

## 4. Correos y personas

- **Patrón de correo:** no lo he averiguado. theHarvester falló porque `bing` no es una fuente soportada y salió con "Invalid source", así que no recogí ni una dirección [E9].
- **Personas:** no he identificado a nadie. En el cuaderno no hay nombres ni cuentas.
- **Lo que sí sé de la organización:**
  - Tiene tiendas por país [E3] y un portal de vendedores en US, EU y BR [E3].
  - Tiene una web de empleo (`careers`, `jobs.careers`) [E3].
  - Usa Trustpilot (por el SPF) [E2] y KnowBe4 (por un TXT) [E2].
  - Existe `security.shein.com`, pero está fuera de alcance [E3, S].
- **Qué haría después (todavía sin hacer):** arreglar theHarvester quitando `bing`, mirar fuentes de empleo y perfiles públicos para sacar nombres del equipo técnico y de seguridad, y deducir el patrón del correo a partir de ahí.

---

## 5. Puntos de interés (por orden)

Estos tres son **hipótesis** basadas solo en el nombre de los hosts. Antes de nada, en la fase activa tengo que resolver el DNS y ver cuáles están vivos (ahora no tengo IP para ellos [E3]), y mantenerme siempre dentro del alcance [S].

1. **`bankltd-test01.shein.com` y `www.bankltd-test01.shein.com`** [E3]. Son los únicos con "test" en el nombre. Los entornos de pruebas suelen estar peor protegidos que los de producción. Lo de "bank" me hace pensar en algo de pagos, pero es solo una suposición. Junto con `privatelift`, `playback` e `ipp` [E3] forman el grupo de hosts de aspecto interno.
2. **VPN: `vpn`, `euvpn`, `usvpn` (y las versiones con `www.`)** [E3]. Una VPN expuesta a internet es una puerta de entrada a redes internas. Miraría qué portal de acceso es, qué producto y versión usa y cómo se autentica. También `euqs` [E3], que no sé qué es.
3. **APIs, callbacks y chat: `api-gateway-central-dc`, `api-service`, `api-shein`, `api-cmc`, `callback-api`, `gateway`, `static.gateway`, `im-api-chat-*`, `im-gateway-chat-*`** [E3]. Aquí está la lógica del negocio y los datos de usuarios. Un `callback-api` podría recibir avisos de terceros (por ejemplo pagos), y el chat en tres regiones implica sesiones, mensajes y quizá subida de archivos. Miraría la autenticación, que un usuario no pueda ver datos de otro, y si las regiones se comportan igual.

**Después de estos tres:** el portal de vendedores (`seller-us/eu/br`, `partner.seller-us`) [E3], porque permite registro de terceros.

---

## Lo que me falta por hacer antes de la fase activa

1. Repetir `security.txt` y `robots.txt` con `https://` bien escrito y en `www.shein.com` [E0, E5].
2. Repetir `dig` pidiendo NS, MX y TXT por separado [E2].
3. Repetir `whois` desde una red con salida o con una web de whois [E1].
4. Resolver el DNS de todos los subdominios de [E3] y comprobar si hay comodín.
5. Preguntar o confirmar si `in.shein.com` y `vn.shein.com` cuentan como alcance, porque shein.in y shein.com.vn están excluidos [E6, S].
6. Arreglar theHarvester (sin `bing`) [E9].
7. Probar las búsquedas con otro buscador, porque Google me pide CAPTCHA y no me deja pasar [E8].
