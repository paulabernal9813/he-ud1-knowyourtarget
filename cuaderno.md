## Fichero security.txt

```
curl https:/shein.com/.well-known/security.txt
<html>
  <head><title>301 Moved Permanently</title></head>
<body>
  <center><h1>301 Moved Permanently</h1></center>
<hr><center>openresty</center>
</body>
</html>
```
## Objetivos

2026-11-03 16:45 · objetivo: shein.com (in scope)
```
$ whois shein.com
connect: Network is unreachable
```

2026-11-03 16:50 · objetivo: shein.com (in scope)
```
$ dig shein.com NS MX TXT +short                                                                       
;; Warning, extra type option
;; Warning, extra type option
"MS=ms73569735"
"MS=ms43134680"
"84b339a2488dacf5abbdab1b9d4e2df849df011fd41afca20a3b75af7d42e40b"
"_2zehtdruk1pleauz30w3ixp6pnbb9kb"
"v=spf1 include:safe-spf01.shein.com include:trustpilotservice.com include:spf-cm.icoremail.net ~all"
"MS=323D6263499D2DA8EE653ACC96AB15F991E6CFD7"
"knowbe4-site-verification=ce9e35a890d24779c787e06232ef670a"
"13.07.2022"
"google-site-verification=SHfTKYZL19Qp2V15tRMVwKxDFZU1X7S2ZPAJbwNpEiY"
"figma-domain-verification=d7c56274a4493f104bcc2549053862a4880565b3737829b150399d55d55c632b-1780388102"
"11y5zhvp5l0jdp10lqlc8l90lg1rk1j2"
"figma-domain-verification=b5b1f3bf1048965bbac743bd313bd78894e2b49aa985b1934aa3dbd9e171f206-1780476658"
"google-site-verification=KdpQinzEpQ7G4WKOoRt6QZOoghgZaJ3Ip6c91mfzwEI"
"google-site-verification=5TESw2i7NQNwfgi-NuDtjH_IogEZD-T6QeEy4OIOgc8"
"cursor-domain-verification-jzxjhk=TFsChZ1PBVvUzfC9MHY4cbCu4"
"google-site-verification=WJ-fVXvfq7EE_DLnVdgpQKNdzrlQH0YOw0r9rXqj78I"
"apple-domain-verification=P3xcqyr8uaKxNDxZ"
"cloudflare_dashboard_sso=5f5be7f603f1b7dbad109cb788a5fbd0"
"google-site-verification=vvaJFFtH6UXXtk_x2QsyPs-jBsKXRe2yLCoFKuGgsOg"

```
2026-11-03 16:53 · objetivo: *.shein.com
```
$ subfinder -d shein.com -silent | tee subs_shein.txt                                                  
my.shein.com
api-gateway-central-dc.shein.com
tracking.news.asia.shein.com
jo.shein.com
im-api-chat-us.shein.com
link-us.shein.com
cn3-mt169.notice.shein.com
careers.shein.com
tracking-us.news.cl.shein.com
count.shein.com
image-tw.shein.com
tracking-us.news.ma.shein.com
tracking.news.pl.shein.com
tracking.news.roe.shein.com
tracking.news.th.shein.com
analytics.shein.com
api-service.shein.com
img.shein.com
link-mx-new.shein.com
eur-exchange-webview.shein.com
im-api-chat-central.shein.com
tracking.news-eur.market.shein.com
nl.shein.com
www.bankltd-test01.shein.com
tracking.news.edmmarket.shein.com
image.email.shein.com
cn3-mt168.notice.shein.com
nz.shein.com
www.playback.shein.com
sg.shein.com
tracking-us.news.th.shein.com
asia.shein.com
ca.shein.com
imag2.shein.com
link-ca.shein.com
ccc-store.shein.com
link-se-new.shein.com
marketplace.shein.com
tracking.news.vn.shein.com
arg.shein.com
es.shein.com
image.shein.com
image-ca.shein.com
img-eur.shein.com
tracking.news.market.shein.com
origin-api-sensors.shein.com
case-studies.seller-us.shein.com
link-nl.shein.com
app.shein.com
id.shein.com
link-it-new.shein.com
www.link-it-new.shein.com
link-tw-new.shein.com
ro.shein.com
seller-br.shein.com
www.api-gateway-central-dc.shein.com
at.shein.com
jobs.careers.shein.com
tracking-us.news.emailmarket.shein.com
tracking.mail.market.shein.com
tracking.news.www.shein.com
emailmarket.shein.com
www.jobs.careers.shein.com
link.shein.com
link-nl-new.shein.com
link-se.shein.com
tracking-us.news.my.shein.com
cn3-mt180.notice.shein.com
roe.shein.com
tracking-us.news.sg.shein.com
ch.shein.com
tracking.news.cl.shein.com
image-mx.shein.com
ma.shein.com
privatelift.shein.com
shop.shein.com
co.shein.com
www.link-mx-new.shein.com
www.link-nl-new.shein.com
tracking.news.my.shein.com
tracking.news.nz.shein.com
pt.shein.com
events.seller-us.shein.com
webinars.seller-us.shein.com
link.emaila.shein.com
gateway.shein.com
it.shein.com
link-news.shein.com
pl.shein.com
playback.shein.com
seller-us.shein.com
th.shein.com
api-shein.shein.com
euvpn.shein.com
link-ru.shein.com
us.help.shein.com
www.analytics.shein.com
tracking.news.ch.shein.com
link.edm.shein.com
link-tw.shein.com
usvpn.shein.com
www.usvpn.shein.com
www.shein.com
de.shein.com
cn3-mt190.info-de.shein.com
www.link-ca-new.shein.com
link-mx.shein.com
exchange.shein.com
www.link-email.shein.com
preferences.shein.com
cl.shein.com
bankltd-test01.shein.com
eur.shein.com
il.shein.com
image-il.shein.com
static.gateway.shein.com
m.shein.com
tracking-us.news.asia.shein.com
im-gateway-chat-central.shein.com
ipp.shein.com
jp.shein.com
link-ca-new.shein.com
api-cmc.shein.com
seller-eu.shein.com
tr.shein.com
im-gateway-chat-eur.shein.com
link-eur-new.shein.com
im-api-chat-eur.shein.com
onelink.shein.com
us.shein.com
link-emailmarket.shein.com
tracking-us.news.ph.shein.com
za.shein.com
mus.help.shein.com
callback-api.shein.com
www.link-eur-new.shein.com
link-market-us.shein.com
www.link-se-new.shein.com
articles.seller-us.shein.com
blog.seller-us.shein.com
img-se.shein.com
tracking-us.news.nz.shein.com
tracking.news.ph.shein.com
link-eur.shein.com
www.link-il-new.shein.com
cinfo-v6.shein.com
security.shein.com
tracking-us.news.vn.shein.com
www.euvpn.shein.com
www.link-market-us.shein.com
www.link-tw-new.shein.com
ph.shein.com
se.shein.com
tracking.news.sg.shein.com
api-sensors.shein.com
br.shein.com
link-il-new.shein.com
www.link-news-new.shein.com
tracking.news.ma.shein.com
ar.shein.com
edm.shein.com
help.shein.com
www.link-emailmarket.shein.com
link-it.shein.com
link-news-new.shein.com
link-email.shein.com
link2.shein.com
cn3-mt182.notice.shein.com
cn3-mt183.notice.shein.com
pe.shein.com
service.shein.com
tracking-us.news.www.shein.com
info.shein.com
ec.shein.com
euqs.shein.com
im-gateway-chat-us.shein.com
img-ru.shein.com
image.nl.shein.com
cn3-mt181.notice.shein.com
tracking-us.news.edmmarket.shein.com
link-de.shein.com
vpn.shein.com
au.shein.com
tracking.news.emailmarket.shein.com
image-it.shein.com
link-fr.shein.com
link-il.shein.com
tracking.mail.market-eur.shein.com
ru.shein.com
s1.shein.com
fr.shein.com
kr.shein.com
link-es.shein.com
cinfo-v4.shein.com
partner.seller-us.shein.com
```

2026-11-03 21:25 · objetivo: shein.com
**IPv4**: 52.39.206.44.
**NameServer**: ns-893.awsdns-47.net.
**Hosting Company**: Amazon - US West (Oregon) datacenter.
**Domain Register**: hichina.com.
**Technology**
| Categoría | Tecnologías mostradas | Para qué se usa |
| --- | --- | --- |
| Cloud & PaaS | Amazon Web Services - EC2 | Cloud computing service (Elastic Compute Cloud) |
| Network | Amazon Web Services - Route 53 | Cloud based Domain Name System (DNS) servie |
| Server-side | SSL | A cryptographic protocol providing communication security over the Internet |
| Client-side (JavaScript / CSS) | Asynchronous Javascript, Session Storage, Local Storage, JavaScript | Widely-supported programming language commonly used to power client-side dynamic content on websites |

2026-11-03 21:30 · objetivo: 
