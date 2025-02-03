"""Pydantic Model for DTO"""
from pydantic import BaseModel

class Result(BaseModel):
    """Result inheriting from Pydantic BaseModel"""
    result: float
   