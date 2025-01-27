from fastapi import APIRouter
from calculator import add, sub, mul

routerCalc  =  APIRouter()


@routerCalc.get("/calc/add/{fst}/{snd}")
async def calc_add(fst:float, snd:float)->dict[str,float]:
    """API to add two  numbers"""

    rst:float = add(fst, snd)
    return {"result": rst}

@routerCalc.get("/calc/sub/{fst}/{snd}")
async def calc_sub(fst:float, snd:float)->dict[str,float]:
    """API to sub two  numbers"""

    rst:float = sub(fst, snd)
    return {"result": rst}

@routerCalc.get("/calc/mul/{fst}/{snd}")
async def calc_sub(fst:float, snd:float)->dict[str,float]:
    """API to mul two  numbers"""

    rst:float = mul(fst, snd)
    return {"result": rst}

@routerCalc.get("/calc/operations/")
async def calc_operations()->dict[str,list[str]]:
    """API to get operations"""

    rst:list[str] = ["add", "mul", "sub"]
    return {"operations": rst}