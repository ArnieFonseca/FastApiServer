"""Calculator API controllers"""

from models.operations import Operations
from services.calculator import add, sub, mul, div
from models.result import Result
from repository.operations import get_operations

async def add_operation(fst:float, snd:float) :
    """API to add two  numbers"""

    rst:Result = Result(result = add(fst, snd))
    return rst

async def sub_operation(fst:float, snd:float) :
    """API to sub two  numbers"""

    rst:Result = Result(result = sub(fst, snd))
    return rst

async def mul_operation(fst:float, snd:float) :
    """API to mul two  numbers"""

    rst:Result = Result(result = mul(fst, snd))
    return rst

async def div_operation(fst:float, snd:float) :
    """API to div two  numbers"""

    rst:Result = Result(result = div(fst, snd))
    return rst

async def retrieve_operations() :
    """API to get operations"""
   
    operationList =  get_operations()
    rst:Operations = Operations(result = operationList)
    
    return rst