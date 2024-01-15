# SQLModel

```python
from pydantic import BaseModel
from sqlmodel import SQLModel, Field

class Pokemon(BaseModel):
    # id: int | None = Field(default=None, primary_key=True) 
    pokedex_number: int
    name: str
    classification: str
    type1: str
    type2: str
    weight: float
    height: float 
```
