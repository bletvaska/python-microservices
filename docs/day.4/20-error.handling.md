# REST API Error Handling

Ak sa pozrieme na stavový kód HTTP požiadavky, tak prídeme na to, že je `200`. Pri nenájdení požiadavky by sme však mali
vrátiť HTTP kód `404`.

```python
@router.get('/api/measurements/{slug}')
def get_last_measurement(slug: int, session: Session = Depends(get_session)):
   statement = select(Measurement).where(Measurement.id == slug)
   measurement = session.exec(statement).one_or_none()

   if measurement is None:
        raise HTTPException(
             status_code=404,
             detail=f'Measurement with number {slug} not found.',
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

```json
{
    "error": {
        "code": 191,
        "fbtrace_id": "Avr5QjIdTnvjvGm3MkuFqVD",
        "message": "Missing redirect_uri parameter.",
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
@router.get('/api/measurements/{number}')
def get_last_measurement(number: int, session: Session = Depends(get_session)):
   statement = select(Measurement).where(Measurement.id == number)
   measurement = session.exec(statement).one_or_none()

   if measurement is None:
      raise HTTPException(
         status_code=404,
         detail=f'Measurement {number} not found.',
      )

   return measurement
```

```python
@router.get('/api/measurements/{slug}', summary='Get measurement detail.', response_model=Measurement)
def get_last_measurement(slug: int, session: Session = Depends(get_session)):
   statement = select(Measurement).where(Measurement.id == slug)
   measurement = session.exec(statement).one_or_none()

   if measurement is None:
        content = ProblemDetails(
            status=404,
            title='File not found',
            detail=f"File with slug '{slug}' does not exist.",
            instance=f'/api/v1/files/{slug}'
        )

        return JSONResponse(
            status_code=content.status,
            media_type='application/problem+json'
            content=content.dict()
        )
```


## Content-type odpovede

podla RFC 7807 ma byt content type odpovede ``. mozeme si teda urobit vlastny navratovy typ.


## Podpora vo FastAPI

* [fastapi-rfc7807](https://pypi.org/project/fastapi-rfc7807/) - prevadza serverove chyby na RFC7807


## Links

* [Best Practices for REST API Error Handling](https://www.baeldung.com/rest-api-error-handling-best-practices)
* [Problem Details for Better REST HTTP API Errors](https://codeopinion.com/problem-details-for-better-rest-http-api-errors/)
* [The Ultimate FastAPI Tutorial Part 5 - Basic Error Handling](https://christophergs.com/tutorials/ultimate-fastapi-tutorial-pt-5-basic-error-handling/)
* [FastAPI: Handling Errors](https://fastapi.tiangolo.com/tutorial/handling-errors/)


