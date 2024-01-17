from pydantic import BaseModel, AnyHttpUrl

from weather.models.measurement import Measurement


class Pager(BaseModel):
    results: list[Measurement] = []
    next: AnyHttpUrl = None
    previous: AnyHttpUrl = None
    first: AnyHttpUrl = None
    last: AnyHttpUrl = None
    count: int = 0
