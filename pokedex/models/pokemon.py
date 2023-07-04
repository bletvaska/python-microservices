from sqladmin import ModelView
from sqlmodel import SQLModel, Field


class Pokemon(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)  # primarny kluc
    name: str  # meno pokemona
    type1: str # typ pokemona
    type2: str | None
    weight: float | None  # hmotnost
    height: float | None  # vyska
    pokedex_number: int  # id pokemona v pokedexe
    classification: str


class PokemonAdmin(ModelView, model=Pokemon):
    page_size = 20
    icon = 'fa-solid fa-spaghetti-monster-flying'
    column_searchable_list = [Pokemon.name]
    column_sortable_list = [Pokemon.name, Pokemon.type1, Pokemon.type2]
    column_list = [
        Pokemon.pokedex_number,
        Pokemon.name,
        Pokemon.type1,
        Pokemon.type2,
        Pokemon.weight,
        Pokemon.height
    ]
