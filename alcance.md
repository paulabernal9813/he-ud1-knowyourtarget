# Alcance del programa · SHEIN (HackerOne)

## 1. Programa elegido

- **Organización:** SHEIN (tienda online internacional de moda)
- **Plataforma:** HackerOne
- **Enlace al programa:** https://hackerone.com/shein
- **Enlace a la página de alcance:** https://hackerone.com/shein/policy_scopes?type=team
- **Tipo:** Bug bounty (hay recompensa económica; la política habla de un "Time to Bounty" de 5 días laborables)
- **Fecha de consulta:** 2026-11-12

## 2. Qué está dentro del alcance (in scope)

| Tipo | Activo |
|------|--------|
| Aplicación web | `*.shein.com` |
| Aplicación web | `*.romwe.com` |
| App Android | `com.zzkko` (SHEIN) |
| App Android | `com.romwe` (ROMWE) |
| App iOS | `878577184` |
| App iOS | `1080248000` |

La política dice que los dominios incluyen sus "sitios localizados" (por ejemplo, las versiones por país). Además explica que `*.shein.com` y `*.romwe.com` comparten parte del desarrollo del backend, así que si el mismo fallo sale en los dos solo se paga completo el primer informe y el segundo cobra el 25 %. Esto me importa poco en el reconocimiento pasivo, pero me sirve para entender que son dos "marcas" con infraestructura parecida.

**En este proyecto solo trabajo con `shein.com` (web).** No he tocado las apps móviles ni `romwe.com`.

## 3. Qué está fuera del alcance (out of scope)

El programa no da una lista de dominios excluidos. Lo que excluye son **tipos de vulnerabilidades** (por ejemplo, XSS reflejado y DOM, clickjacking en páginas sin acciones sensibles, falta de cabeceras de buenas prácticas, SPF/DMARC mal configurados, divulgación de versión de software, etc.).

Hay dos puntos que sí afectan a los dominios y que me parecen importantes:

1. **Subdominios que apuntan a servicios de terceros.** Si un dominio de SHEIN resuelve a un servicio alojado por otra empresa (Zendesk, Emarsys…), los fallos de ese tercero no se aceptan porque SHEIN no puede arreglarlos. Hay que reportarlos al tercero.
2. **Subdominios "abandonados" (subdomain takeover).** Un dominio cuyo DNS no se borró a tiempo y apunta a otro servicio no se acepta, salvo que se demuestre que de verdad se puede tomar y alojar contenido malicioso.

Todo lo que no sea `*.shein.com` o `*.romwe.com` (u otras empresas) queda fuera, y el dominio raíz `shein.com` hay que mirar bien cómo lo trata el scope-guard con un comodín (ver apartado 5).

## 4. Reglas que afectan a este proyecto

| Regla de la política | Cómo me afecta |
|----------------------|----------------|
| No hay prohibición expresa de herramientas automáticas ni límite de peticiones | Aun así, en este proyecto solo uso **técnicas pasivas** (la regla del enunciado manda más que la del programa) |
| Cualquier actividad que pueda causar una interrupción del servicio (DoS) está fuera de alcance | No hago escaneos ni nada que pueda saturar nada |
| **Ingeniería social prohibida** (phishing, vishing, smishing) | No hablo con empleados ni creo cuentas falsas |
| Hay que evitar violaciones de privacidad, destrucción de datos y degradación del servicio | Si veo algo sensible lo anoto sin copiar el dato y aviso al profesor |
| Solo se puede interactuar con cuentas propias o con permiso explícito del dueño | No me hace falta, no creo cuentas en SHEIN |
| Se recomienda registrar una cuenta con el alias de HackerOne (`usuario@wearehackerone.com`) | No aplica: en este proyecto no creo cuentas en los servicios del objetivo |
| Informes con pasos reproducibles, una vulnerabilidad por informe | Lo tengo en cuenta por si hay que reportar algo grave; se haría por el canal de HackerOne |
| **Safe harbor:** lo que se haga siguiendo la política se considera conducta autorizada | Es justo lo que dice el enunciado: el alcance es la frontera legal |
| No hay requisito de identificación ni prohibición de contactar con empleados más allá de la ingeniería social | De todas formas, no contacto con nadie |

## 5. Cómo lo paso a `scope.txt`

Tomando `*.shein.com` como mi objetivo:

```
# scope.txt · programa: SHEIN (HackerOne) · consultado: 2026-11-12
*.shein.com
```

Cosas que he pensado al hacerlo:

- Con un comodín `*.shein.com`, el scope-guard de ejemplo del enunciado trata el dominio raíz (`shein.com`) como **fuera**, igual que `empresa.com` con `*.empresa.com`. Como el programa también cubre el dominio principal, si quiero consultar `shein.com` tengo que añadirlo como línea aparte (`shein.com`). Hay que comprobar cómo quedó mi `scope.txt` real y que el agente solo consultó lo que debía.
- No hay exclusiones expresas en la política. Podría excluir por precaución los subdominios que van a terceros (`help.shein.com` → Zendesk, `analytics.shein.com`, `image.shein.com`, `service.shein.com`…), pero es una decisión mía y no del programa, así que de momento no los excluyo y los trato con cuidado en el mapa.
- `romwe.com` y las apps quedan fuera de mi `scope.txt` aunque el programa las admita, porque no las voy a trabajar.

## 6. Resumen

SHEIN es un bug bounty con alcance amplio (comodines `*.shein.com` y `*.romwe.com`, más apps), con safe harbor y con una lista larga de vulnerabilidades excluidas. Lo más importante para mí es: ingeniería social prohibida, no provocar caídas del servicio y tener cuidado con los dominios que en realidad son servicios de terceros.
