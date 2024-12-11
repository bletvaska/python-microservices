from weather.responses import ProblemDetailsResponsefrom litecli.packages.special.dbcommands import status

# REST API Error Handling

Ak sa pozrieme na stavový kód HTTP požiadavky, tak prídeme na to, že je `200`. Pri nenájdení požiadavky by sme však mali
vrátiť HTTP kód `404`.

```python
@router.get('/{city}/last')
async def get_last_measurement(city: str,
                               session: Annotated[Session, Depends(get_db_session)]):
    statement = select(Measurement).where(func.lower(Measurement.city) == city.lower()).order_by(Measurement.dt.desc())
    measurement = session.exec(statement).first()

    if measurement is None:
        raise HTTPException(
             status_code=HTTPStatus.NOT_FOUND,
             detail=f'There are no measurements for city {city}.',
         )

   return measurement
```


## Chyby iných službách

Pozrime sa na to, ako chyby riešia iné služby:

### Default Spring Error Responses

```json
{
    "timestamp":"2019-09-16T22:14:45.624+0000",
    "status":500,
    "error":"Internal Server Error",
    "message":"No message available",
    "path":"/api/book/1"
}
```


### Twitter

request:

```bash
$ http https://api.twitter.com/1.1/statuses/update.json?include_entities=true
```

response:

```http request
HTTP/1.1 400 Bad Request
```

```json
{
    "errors": [
        {
            "code": 215,
            "message": "Bad Authentication data."
        }
    ]
}
```


### Facebook

request:

```bash
$ http 'https://graph.facebook.com/oauth/access_token?client_id=foo&client_secret=bar&grant_type=baz'
```

response:

```http request
HTTP/1.1 400 Bad Request
```

```json
{
    "error": {
        "code": 100,
        "fbtrace_id": "A6a08PZwgApfrkl5aYEaioI",
        "message": "Invalid grant_type: 'baz'. Supported types: authorization_code, client_credentials",
        "type": "OAuthException"
    }
}
```


## Standardized Response Bodies

* the IETF devised [RFC 7807](https://tools.ietf.org/html/rfc7807), which creates a generalized error-handling schema

* This schema is composed of five parts:

  * `type` – a URI identifier that categorizes the error
  * `title` – a brief, human-readable message about the error
  * `status` – the HTTP response code (optional)
  * `detail` – a human-readable explanation of the error
  * `instance` – a URI that identifies the specific occurrence of the error

* example:

  ```json
  {
    "type": "/errors/incorrect-user-pass",
    "title": "Incorrect username or password.",
    "status": 401,
    "detail": "Authentication failed due to incorrect username or password.",
    "instance": "/login/log/abc123"
  }
  ```


## Vlastny Model

Vytvorime si vlastny model pre reprezentaciu chyb podla RFC 7807 s nazvom `problem_details.py` v balicku `fishare.models`:

```python
from pydantic import BaseModel


class ProblemDetails(BaseModel):
    type = "about:blank"
    title: str
    status: int | None
    detail: str | None
    instance: str | None
```


## Pouzitie modelu

pri vyhladavani suboru podla slug-u mozeme v pripade, ze sa subor nenasiel, skoncit s HTTP kodom stavu 404 takto:



```python
@router.get('/{city}/last')
async def get_last_measurement(city: str,
                               session: Annotated[Session, Depends(get_db_session)]):
    statement = select(Measurement).where(func.lower(Measurement.city) == city.lower()).order_by(Measurement.dt.desc())
    measurement = session.exec(statement).first()

    if measurement is None:
        content = ProblemDetails(
            status=HTTPStatus.NOT_FOUND,
            title='File not found',
            detail=f"File with slug '{city}' does not exist.",
            instance=f'/api/{city}/last'
        )

        return JSONResponse(
            status_code=content.status,
            media_type='application/problem+json',
            content=content.model_dump()
        )
```


## Content-type odpovede

podla RFC 7807 ma byt content type odpovede `application/problem+json`. mozeme si teda urobit vlastny navratovy typ.

Za tymto ucelom vytvorime novy modul s nazvom `responses.py` a v nom vytvorime novy typ odpovede `ProblemDetailsResponse`.


```python
from fastapi.responses import JSONResponse

class ProblemDetailsResponse(JSONResponse):
    media_type = "application/problem+json"
```

A toto nam staci na to, aby sme ho vedeli pouzit nasledovne:

```python
@router.get('/{city}/last')
async def get_last_measurement(city: str,
                               session: Annotated[Session, Depends(get_db_session)]):
    statement = select(Measurement).where(func.lower(Measurement.city) == city.lower()).order_by(Measurement.dt.desc())
    measurement = session.exec(statement).first()

    if measurement is None:
        problem = ProblemDetails(
            status=HTTPStatus.NOT_FOUND,
            title="Measurement not found",
            detail="Probably measurements for given city were not found in database. That means, the city doesnt exist or the measurements were not collected yet.",
            instance=f'/{city}/last'
        )

       return ProblemDetailsResponse(
          status_code=problem.status,
          content=problem.model_dump()
       )

    return measurement
```

Miesto toho ale mozeme upravit typ odpovede este viac:

```python
class ProblemDetailsResponse(JSONResponse):
    media_type = "application/problem+json"

    def __init__(
        self,
        title: str,
        detail: str,
        instance: str,
        status_code: int = 200,
        media_type: str | None = None,
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
                         media_type,
                         background)
```

A v kode to potom pouzijeme takto:

```python
@router.get('/{city}/last')
async def get_last_measurement(city: str,
                               session: Annotated[Session, Depends(get_db_session)]):
    statement = select(Measurement).where(func.lower(Measurement.city) == city.lower()).order_by(Measurement.dt.desc())
    measurement = session.exec(statement).first()

    if measurement is None:
        return ProblemDetailsResponse(
            status_code=HTTPStatus.NOT_FOUND,
            title="Measurement not found",
            detail="Probably measurements for given city were not found in database. That means, the city doesnt exist or the measurements were not collected yet.",
            instance=f'/{city}/last'
        )

    return measurement
```


## Podpora vo FastAPI

* [fastapi-rfc7807](https://pypi.org/project/fastapi-rfc7807/) - prevadza serverove chyby na RFC7807


## Links

* [Best Practices for REST API Error Handling](https://www.baeldung.com/rest-api-error-handling-best-practices)
* [Problem Details for Better REST HTTP API Errors](https://codeopinion.com/problem-details-for-better-rest-http-api-errors/)
* [The Ultimate FastAPI Tutorial Part 5 - Basic Error Handling](https://christophergs.com/tutorials/ultimate-fastapi-tutorial-pt-5-basic-error-handling/)
* [FastAPI: Handling Errors](https://fastapi.tiangolo.com/tutorial/handling-errors/)


