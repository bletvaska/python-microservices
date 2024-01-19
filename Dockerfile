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
