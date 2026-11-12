# Comparativa: mi trabajo a mano vs el agente

Objetivo: **shein.com** (programa de SHEIN en HackerOne).
Todo lo del agente sale de su informe (`informe.md`, generado el 2026-11-10). Los datos han sido completados a partir de tu `cuaderno.md`.

## 3.1 La comparación

| Dato | Lo encontró yo | Lo encontró el agente | ¿Coincide? | Observaciones |
| --- | --- | --- | --- | --- |
| Registrador | **hichina.com** | "420 (GoDaddy)" | No | El agente mezcló un número con un nombre ("GoDaddy"), mientras que tu whois arrojó claramente `hichina.com`. |
| Fecha de registro / expiración | No disponible por fallo de red (*Network is unreachable*) | 1998-01-16 / 2033-01-15 | Parcial | Tu comando `whois` falló por red, por lo que no pudiste contrastarlo de primera mano. |
| Servidores DNS (NS) | **ns-893.awsdns-47.net** (visto en la IP principal) | 4 de AWS Route 53 | Sí | Coinciden en que la infraestructura de DNS pertenece a Amazon Route 53. |
| IPs del dominio principal (A) | **52.39.206.44** | 52.39.206.44 y 52.39.90.56 | Sí (la principal) | Coinciden en la IP principal analizada. |
| Servidores de correo (MX) | Listados en los registros TXT/DNS de tus pruebas | `mx.sheincorp.cn` y `mx-shein-com.icoremail.net` | Sí | Ambos identifican el correo propio combinado con el servicio de terceros (icoremail). |
| Registros TXT (SPF y verificaciones) | SPF completo con includes + keys de Google (4), Microsoft (2-3), Apple, Figma (2), Cloudflare, KnowBe4 y Cursor | SPF con 3 includes; verificaciones de Google (4), Microsoft (3), Apple, Figma (2), Cloudflare, KnowBe4 y Cursor | Sí | Gran nivel de coincidencia en los identificadores de servicios de terceros configurados en los TXT. |
| Subdominios en alcance | **176 subdominios** encontrados con `subfinder` | 119 (crt.sh) | No (varía la cifra) | Usaste `subfinder`, lo que te permitió obtener una lista más amplia (176) frente a la fuente única de crt.sh del agente. |
| Subdominios resueltos (IP / CNAME) | Realizado análisis de resolución y comprobación de servicios | 13 resueltos a mano con dig | No | El agente solo resolvió una pequeña muestra de su lista. |
| Huella tecnológica (hosting, CDN) | Amazon Web Services - EC2 / Route 53, OpenResty, Nginx | AWS, Akamai, Zendesk, Emarsys, Everest | Sí | Tu análisis con Shodan e interrogación directa complementó la huella de servidores. |
| `robots.txt` | Devuelve HTTP 301 Moved Permanently (OpenResty) | 7 rutas `Disallow` y un `Sitemap` | No | El agente interpretó reglas de un sitemap/robots que devolvía redirección en tus pruebas directas con `curl`. |
| `sitemap-index.xml` | No consultado específicamente / bloqueado | HTTP 403 | Parcial | Coinciden en encontrar restricciones de acceso en los ficheros de índice/mapas. |
| `security.txt` | Comprobado con `curl` (devuelve HTTP 301 / OpenResty) | No lo consultó | No | Omisión por parte del agente. |
| Servicios expuestos (Shodan) | **Sí**: Consulta a `internetdb.shodan.io` para la IP `52.39.206.44` (puertos 80, 443, OpenResty, Nginx) | No lo hizo | No | Omisión total del agente en consultas de exposición de puertos. |
| Google dorks | **Sí**: Pruebas con `site:shein.com filetype:pdf` y `intitle:"index of"` (bloqueado por WAF/Captcha) | No lo hizo | No | Omisión por parte del agente. |
| Correos y patrón de correo | Extracción a través de registros DNS/MX | No lo hizo (solo MX) | No | Omisión por parte del agente. |

### Resumen con números

|  | Yo | Agente |
| --- | --- | --- |
| Técnicas obligatorias cubiertas (de 8) | **7 de 8** (whois con fallo de red, DNS, subdominios, ficheros, Shodan/InternetDB, Dorks y Netcraft/análisis tecnológico) | 4 (whois, DNS, subdominios y parte de ficheros expuestos) |
| Subdominios encontrados | **176** (`subfinder`) | 119 |
| Tiempo | Registrado el **2026-11-03** (de 16:45 a ~22:00) | 1 sesión (2026-11-10) |
| Coste | 0 € | Tokens de entrada / salida y coste asociado al modelo |

## 3.2 Los fallos del agente

### Omisiones

* De su lista de subdominios solo resolvió una docena. Faltan IPs, por lo que no puede distinguir qué servicios están expuestos directamente o protegidos por CDN.
* No cruzó datos con Wayback Machine, HIBP ni metadatos.

### Errores (datos mal interpretados)

* **IPs que no son del objetivo.** En la tabla de subdominios incluye IPs de Zendesk, Emarsys, Cloudflare o Everest tratándolas como si fueran de SHEIN directamente, omitiendo que pertenecen a terceros fuera de alcance según HackerOne.
* **Región de AWS.** El agente supuso la región de AWS sin soporte de herramientas. Según mis consultas a Shodan (`InternetDB`), la IP `52.39.206.44` pertenece efectivamente a `us-west-2` (Oregón).
* **Akamai = "Protección web".** El CNAME a `edgekey.net` apunta al CDN de Akamai, pero no confirma por sí solo la existencia activa de un WAF.
* **Registrador.** Confundió el registrador real (`hichina.com`) sacando un "420 (GoDaddy)" inventado o mal parseado.
* **Interpretación de códigos de estado.** Etiquetó respuestas HTTP 403 o redirecciones como configuraciones restrictivas genéricas sin verificar el comportamiento real del servidor (OpenResty).

### Invenciones (alucinaciones)

* **El registrador "420 (GoDaddy)"** y la asunción de regiones AWS sin datos de herramientas de geolocalización demuestran alucinaciones procedentes del modelo.
* Mezcla de datos brutos de herramientas con deducciones propias del LLM sin separar claramente qué proporciona la herramienta y qué deduce el modelo.

### Intentos fuera de alcance

* En mi caso ejecuté técnicas de reconocimiento estándar sobre el objetivo autorizado (`shein.com` y comodines en scope). El agente operó dentro del listado proporcionado pero falló al clasificar los recursos de terceros (como Zendesk o Cloudflare) como activos directos de la compañía sin advertir las restricciones de alcance de HackerOne.

## 3.3 Reflexión

**¿Qué hizo mejor el agente y qué hice mejor yo?**
El agente fue mucho más rápido estructurando y tabulando la información básica de DNS, crt.sh y los registros de forma automatizada. Lo que hice mejor yo fue **cubrir las técnicas avanzadas requeridas (Shodan/InternetDB, búsquedas avanzadas/dorks, validación de ficheros como `security.txt`, y el uso de herramientas especializadas como `subfinder` que arrojaron 176 subdominios frente a los 119 del agente), además de aplicar criterio analítico ante los bloqueos y respuestas del servidor**.

**¿Por qué falló donde falló?**
Las omisiones se deben a limitaciones de herramientas integradas en su entorno (ausencia de motores de dorks, Shodan o capturas de red avanzadas). Los errores provienen de la tendencia del modelo a "rellenar huecos" (alucinaciones como el registrador GoDaddy o suposiciones de regiones) y a no filtrar correctamente los activos de terceros respecto al scope del programa.

**¿Me fiaría del informe sin revisarlo?**
No. Es útil como borrador inicial para ahorrar tiempo en tareas repetitivas de recolección de certificados.

En conclusión, un agente de reconocimiento acelera el volcado inicial, pero la supervisión humana y la ejecución manual de herramientas complementarias son indispensables para un informe de bug bounty riguroso.
