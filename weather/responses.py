import typing

from fastapi.responses import JSONResponse
from starlette.background import BackgroundTask

from weather.models.problem_details import ProblemDetails


class ProblemDetailsResponse(JSONResponse):
    def __init__(
        self,
        title: str,
        detail: str,
        instance: str,
        status_code: int = 500,
        headers: typing.Mapping[str, str] | None = None,
        background: BackgroundTask | None = None,
    ) -> None:
        problem = ProblemDetails(
            title=title,
            detail=detail,
            instance=instance,
            status=status_code,
        )

        super().__init__(problem.model_dump(),
                         status_code,
                         headers,
                         "application/problem+json",
                         background)
