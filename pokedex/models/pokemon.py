from sqlmodel import SQLModel, Field


class Pokemon(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)  # primarny kluc
    name: str  # meno pokemona
    type1: str  # typ pokemona
    type2: str
    weight: float  # hmotnost
    height: float  # vyska
    pokedex_number: int  # id pokemona v pokedexe
