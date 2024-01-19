FROM python:3.12-slim
LABEL authors="mirek"

COPY dist/*whl /wheels/

RUN apt update
RUN apt install --yes httpie

RUN pip install --upgrade pip \
    && pip install /wheels/*whl \
    && rm -rf /wheels

# WORKDIR /app
# VOLUME [ "/app" ]

HEALTHCHECK \
    --interval=15s \
    --timeout=3s \
    --retries=3 \
    --start-period=5s \
    CMD http --check-status get http://localhost:8000/unhealthy || exit 1

EXPOSE 8000

#CMD [ "weather" ]
CMD [ "uvicorn", "weather.main:app", "--host", "0.0.0.0", "--log-level", "error" ]
