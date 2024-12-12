# Zbieranie metrík


## Inštalácia modulu `starlette-prometheus`

Pre jednoduchosť použijeme [Starlette Prometheus](https://github.com/perdy/starlette-prometheus), ktorý
nainštalujeme príkazom:

```bash
$ poetry add starlette-prometheus
```


## Aktualizácia kódu

Do našej aplikácie následne stačí pridať tento fragment kódu:

```python
from starlette_prometheus import metrics, PrometheusMiddleware

app = FastAPI()
app.add_middleware(PrometheusMiddleware)
app.add_route("/metrics", metrics)
```


## Otestovanie

endpoint s metrikami mozeme otestovat pomocou HTTP klienta `httpie`:

```bash
$ http http://$HOSTIP:8000/metrics
```
