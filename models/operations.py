"""Pydantic Model for DTO of operations"""
from pydantic import BaseModel

class Operations(BaseModel):
    """Operation inheriting from Pydantic BaseModel"""
    result: list[str]
   