# Health Check API


![Health Check](../images/health.check.jpg)


## Problem

* spravovať distribuované systémy je náročné. skladajú sa totiž z veľkého množstva súčastí, ktoré potrebujú pracovať (a spolupracovať), aby systém mohol ako celok fungovať.

* ak sa niektorá jeho súčať pokazí, systém ju musí:

    * detegovať, napr. vytvorením alertu,
    * obísť ju, napr. load balancer nebude posielať požiadavky na nefungujúcu službu, a
    * opraviť ju, resp. zotaviť sa z nej.

* a to všetko sa musí udiať automagicky.

* ako teda detegovať, že bežiaca služba nedokáže spracovávať požiadavky?


## Health Check

### Overview

* **health check** poskytuje jednoduchý mechanizmus, pomocou ktorého je možné overiť, či daná služba pracuje správne. obyčajne má služba vytvorené **Health Check API** pomocou protokolu HTTP (napr. `/health`), ktorá pomocou stavových kódov hovorí o stave služby. Je možné sa však stretnúť aj s prípadmi, kedy sa kontrola stavu služby vykonáva pomocou metódy `HEAD` nad niektorým existujúcim endpointom.

* okrem stavového kódu sa môže vo výsledku HTTP požiadavky nachádzať aj krátky JSON dokument, ako napr.:

  ```json
  {
      "status" : "UP"
  }
  ```

* v rámci kontroly zdravia služby sa môže overovať napr.:

    * stav spojenia s ostatnými službami,
    * stav stroja, napr. jeho diskový priestor, využitie pamäte a pod.,
    * špecifická logika aplikácie,
    * stav databázy,
    * a iné.


### Health Check in Containers

* okrem toho však s kontrolou stavu súvisí aj kontrola stavu kontajnera, v ktorom je aplikácia spustená. kontajnery totiž bežia 24/7 a aj tu môže dôjsť k niektorým situáciám:

    * stav kontajneru
    * aktualizácia aplikácie v kontajneri

* takže ak aplikácia beží v kontajneri a ten je spustený, nemusí to hneď znamenať, že aplikácia vo vnútri kontajneru parcuje správne. kontrolu teda treba vykonávať ako na úrovni aplikácie, tak aj na úrovni kontajnera.


### Health Check in Virtual Machines

* Tento prístup však nie je vhodný, ak je služba/aplikácia spustená vo virtuálnom stroji. Zmazanie a vytvorenie kontajnera nanovo je totiž výrazne rýchlejšia operácia ako v prípade reštartovania celého virtuálneho stroja. Zmazať a znovu vytvoriť virtuálny stroj môže trvať aj hodiny.

* V tomto prípade treba zvoliť iný prístup - napr. pomocou **Watch dog**-u.


### Health Checks Interval

* V rámci kontroly zdravia služby, sa _Health Check API_ dopytuje v pravidelných intervaloch. Môže to robiť ďalšia monitorovacia služba alebo orchestračný nástroj, ako je napr. _Kubernetes_.

* Samozrejme k problému môže dôjsť vtedy, ak služba zlyhá medzi dvoma kontrolami. Takže k odhaleniu zlyhania nedôjde okamžite pri jeho vzniku, ale až pri ďalšej kontrole.


## Health Check in Kubernetes Cluster

* ak sa rozprávame o nasadení niektorej služby v K8s klastri, ten na kontrolu stavu používa dve sondy, resp. dva typy kontroly zdravia služieb:

    * **readiness**
    * **liveness**

* Je dôležité rozumieť ako ich rozdielu, tak aj tomu, kedy ich použiť.


## Summary

* health check je požiadavka na každý distribuovaný systém

    * zvyšujú spoľahlivosť
    * zvyšujú dostupnosť


## Additional links

* [Pattern: Health Check API](https://microservices.io/patterns/observability/health-check-api.html)
* [Using a health check in Node.js apps](https://cloud.ibm.com/docs/node?topic=node-node-healthcheck)
* [FastAPI Health](https://github.com/Kludex/fastapi-health)
* [py-healthcheck](https://pypi.org/project/py-healthcheck/)
* Youtube: [Kubernetes Health Checks with Readiness and Liveness Probes](https://www.youtube.com/watch?v=mxEvAPQRwhw)
* [Configure Liveness, Readiness and Startup Probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/)
* https://microservices.io/patterns/observability/health-check-api.html
