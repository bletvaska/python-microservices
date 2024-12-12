FROM python:3.12-slim

LABEL authors="mirek"

COPY dist/weather-2024.2.2-py3-none-any.whl /wheels/

RUN pip install /wheels/*whl

EXPOSE 8000

# ENTRYPOINT python3 /app/app.py
CMD [ "start_app" ]
# CMD ["uvicorn", "weather.main:main", "--host", "0.0.0.0", "--port", "8000" ]
# CMD [ "python", "-m", "weather" ]
