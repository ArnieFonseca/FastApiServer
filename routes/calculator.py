from fastapi import APIRouter
from services.calculator import  add, sub, mul, div
from models.result import Result
from models.operations import Operations

# default preix to calc and taag the API Documentation
routerCalc  =  APIRouter(
    tags=["Calculator"], 
    prefix="/calc")


@routerCalc.get("/add/{fst}/{snd}")
async def calc_add(fst:float, snd:float) :
    """API to add two  numbers"""

    rst:Result = Result(result = add(fst, snd))
    return rst


@routerCalc.get("/sub/{fst}/{snd}")
async def calc_sub(fst:float, snd:float) :
    """API to sub two  numbers"""

    rst:Result = Result(result = sub(fst, snd))
    return rst

@routerCalc.get("/mul/{fst}/{snd}")
async def calc_sub(fst:float, snd:float) :
    """API to mul two  numbers"""

    rst:Result = Result(result = mul(fst, snd))
    return rst
 

@routerCalc.get("/div/{fst}/{snd}")
async def calc_div(fst:float, snd:float) :
    """API to div two  numbers"""

    rst:Result = Result(result = div(fst, snd))
    return rst

@routerCalc.get("/operations/")
async def calc_operations():
    """API to get operations"""
     
    rst:Operations = Operations(result = ["add", "mul", "sub", "div"])
    return rst
     