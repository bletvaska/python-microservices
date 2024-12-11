import uvicorn

# start app
uvicorn.run('weather.main:app',
            reload=True,
            host='0.0.0.0',
            port=8000,
            log_config=None,
            log_level=None,
            )
