from fastapi import APIRouter
from services.calculator import  add, sub, mul, div

# default preix to calc and taag the API Documentation
routerCalc  =  APIRouter(
    tags=["Calculator"], 
    prefix="/calc")


@routerCalc.get("/add/{fst}/{snd}")
async def calc_add(fst:float, snd:float)->dict[str,float]:
    """API to add two  numbers"""

    rst:float = add(fst, snd)
    return {"result": rst}

@routerCalc.get("/sub/{fst}/{snd}")
async def calc_sub(fst:float, snd:float)->dict[str,float]:
    """API to sub two  numbers"""

    rst:float = sub(fst, snd)
    return {"result": rst}

@routerCalc.get("/mul/{fst}/{snd}")
async def calc_sub(fst:float, snd:float)->dict[str,float]:
    """API to mul two  numbers"""

    rst:float = mul(fst, snd)
    return {"result": rst}

@routerCalc.get("/div/{fst}/{snd}")
async def calc_div(fst:float, snd:float)->dict[str,float]:
    """API to div two  numbers"""

    rst:float = div(fst, snd)
    return {"result": rst}

@routerCalc.get("/operations/")
async def calc_operations()->dict[str,list[str]]:
    """API to get operations"""

    rst:list[str] = ["add", "mul", "sub", "div"]
    return {"operations": rst}