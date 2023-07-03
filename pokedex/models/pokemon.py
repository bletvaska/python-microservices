from pydantic import BaseModel


class Pokemon(BaseModel):
    id: int  # primarny kluc
    name: str  # meno pokemona
    type1: str  # typ pokemona
    type2: str
    weight: float  # hmotnost
    height: float  # vyska
    pokedex_number: int  # id pokemona v pokedexe
