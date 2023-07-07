from time import time

from fastapi import Request, Response


def add_process_time_to_header(request: Request, call_next) -> Response:
    start = time()
    response: Response = call_next(request)
    duration = time() - start
    response.headers['x-processing-time'] = str(duration * 1000)
    return response
