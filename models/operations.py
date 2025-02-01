from pydantic import BaseModel


class Operations(BaseModel):
    result: list[str]
   