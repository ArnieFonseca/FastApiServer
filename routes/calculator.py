"""Calculator Routes"""
from fastapi import APIRouter
from models.result import Result
from models.operations import Operations
from controllers.calculator import add_operation, sub_operation, mul_operation, div_operation, retrieve_operations

# default prefix to calc and tag the API Documentation
routerCalc  =  APIRouter(
    tags=["Calculator"], 
    prefix="/calc")
"""Calculator Routes end-points"""

@routerCalc.get("/add/{fst}/{snd}")
async def calc_add(fst:float, snd:float) :
    """API to add two  numbers"""

    rst:Result = await add_operation(fst, snd)
    return rst

@routerCalc.get("/sub/{fst}/{snd}")
async def calc_sub(fst:float, snd:float) :
    """API to sub two  numbers"""

    rst:Result = await sub_operation(fst, snd)
    return rst

@routerCalc.get("/mul/{fst}/{snd}")
async def calc_mul(fst:float, snd:float) :
    """API to mul two  numbers"""

    rst:Result = await mul_operation(fst, snd)
    return rst
 

@routerCalc.get("/div/{fst}/{snd}")
async def calc_div(fst:float, snd:float) :
    """API to div two  numbers"""

    rst:Result = await div_operation(fst, snd)
    return rst

@routerCalc.get("/operations/")
async def calc_operations():
    """API to get operations"""

    rst:Operations = await retrieve_operations()
    return rst
     