from sqlmodel import Session, create_engine


def get_session() -> Session:
    engine = create_engine(
        'sqlite:////home/mirek/Documents/kurzy/python-courses/python-microservices/resources/pokedex.sqlite'
    )
    with Session(engine) as session:
        yield session
