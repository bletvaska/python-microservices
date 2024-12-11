# Parameter `request`

```python
@router.get('/{city}/last')
async def get_last_measurement(request: Request,
                               city: str,
                               session: Annotated[Session, Depends(get_db_session)]):
    statement = select(Measurement).where(func.lower(Measurement.city) == city.lower()).order_by(Measurement.dt.desc())
    measurement = session.exec(statement).first()

    if measurement is None:
        return ProblemDetailsResponse(
            status_code=HTTPStatus.NOT_FOUND,
            title="Measurement not found",
            detail="Probably measurements for given city were not found in database. That means, the city doesnt exist or the measurements were not collected yet.",
            instance=request.url.path
        )

    return measurement
```
