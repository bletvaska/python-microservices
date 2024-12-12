FROM python:3.12-slim

LABEL authors="mirek"

RUN groupadd --gid 1000 pythonista \
    && useradd --uid 1000 --gid 1000 --no-create-home pythonista

COPY dist/weather-2024.2.2-py3-none-any.whl /wheels/

RUN apt update \
    && apt install --yes curl \
    && pip install /wheels/*whl

WORKDIR /app
EXPOSE 8000
VOLUME [ "/app" ]
USER pythonista

HEALTHCHECK \
    --interval=10s \
    --timeout=3s \
    --retries=3 \
    --start-period=5s \
    CMD curl --fail http://localhost:8000/healthcheck || exit 1

# ENTRYPOINT python3 /app/app.py
CMD [ "start_app" ]
# CMD ["uvicorn", "weather.main:main", "--host", "0.0.0.0", "--port", "8000" ]
# CMD [ "python", "-m", "weather" ]
