from pydantic import BaseModel


class ProblemDetails(BaseModel):
    type: str = "about:blank"
    title: str
    status: int | None = None
    detail: str | None = None
    instance: str | None = None
