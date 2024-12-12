# Vytvorenie Docker obrazu

## Prva verzia

```dockerfile
FROM python:3.12-slim
LABEL authors="mirek"

COPY dist/*whl /wheels/

RUN pip install --upgrade pip \
    && pip install /wheels/*whl \
    && rm -rf /wheels

# WORKDIR /app
# VOLUME [ "/app" ]

EXPOSE 8000

#CMD [ "weather" ]
CMD [ "uvicorn", "weather.main:app", "--host", "0.0.0.0", "--log-level", "error" ]
```

vytvorime obraz:

```bash
$ docker image build --tag weather .
```
a spustime:

```bash
$ docker container run -it --rm --publish 8000:8000 --env-file .env weather
```


## Best Practices - Separate User

```dockerfile
RUN groupadd --gid 1000 maker \
    && useradd --uid 1000 --gid 1000 --no-create-home maker \
    && pip3 install apprise loguru paho-mqtt pydantic pydantic-settings

USER maker
```

otestovat:

```bash
$ docker container exec --it notifier id
```


## Best Practices - Healthcheck

```dockerfile
HEALTHCHECK \
    --interval=30s \
    --timeout=10s \
    --retries=3 \
    CMD curl -d http://localhost:8000/healthcheck || exit 1
```
