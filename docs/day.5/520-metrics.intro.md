# O metrikách


## Čo sú to metriky?

Metriky poskytujú pohľad na aktuálny stav vašej aplikácie. Prípadne vieme pomocou metrík zistiť stav v čase.

ale to nie je vsetko. okrem toho vám metriky povedia:

* či je vaša služba zdravá a pracuje správne
* čo je zle
* čo je dobre
* čo sa čoskoro pokazí
* kam sa treba pozerať


## Z čoho sa skladá vzorka metriky

Vzorka metriky sa skladá z týchto troch častí (viď obrázok vyššie):

* **Name** - Názov metriky, ako napr. jvm_memory_max_bytes, placed_orders
* **Value** - Číselná hodnota.
* **Timestamp** - Čas merania vzorky.

Okrem toho niektore monitorovacie systemy maju podporu pre tzv. **dimenzie** (metadáta, značky). Jedná sa o dvojice
meno-hodnota / kluc-hodnota, do ktorych sa pridávajú dalsie rozsirujuce informacie. Tieto sa následne pouzivaju pre
agregovanie udajov na zaklade zvolených dimenzii.


## (Four) Golden Signals

Golden signals are an effective way of monitoring the overall state of the system and identifying problems. Ak máte
 možnosť zaznamenávať len pár z nich, určite monitorujte zlatú štvoricu: **latency**, **traffic**, **errors**, and
**saturation**.
