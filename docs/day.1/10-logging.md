# Logovanie

* co je to logovanie?
* urovne logovacich sprav
* nasa mikrosluzba sa bude spustat v kontajneri
  * odporucanie je logovat na standardny vystup
* python ma podporu pre logovanie v standardnej kniznici
  * je komplexna
  * zvlada aj rotovanie log suboro
  * je potrebne poznat aj dalsie veci, ako handler, logger, formatter
* my pouzijeme nieco jednoduchsie - modul loguru

instalacia

```bash
$ poetry add loguru
```

pouzitie

```python
from loguru import logger

logger.info('New connection')
```
