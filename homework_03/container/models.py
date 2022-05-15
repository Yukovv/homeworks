from pydantic import BaseModel


class Stuff(BaseModel):
    name: str
    amount: int = 1
