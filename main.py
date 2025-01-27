from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from calculator import add, sub, mul

app = FastAPI()


# @app.get("/")
# async def root():
#     return {"message": "Welcome to Fast API for Python"}
origins = [

    "http://localhost:4200"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/calc/add/{fst}/{snd}")
async def calc_add(fst:float, snd:float)->dict[str,float]:
    """API to add two  numbers"""

    rst:float = add(fst, snd)
    return {"result": rst}

@app.get("/calc/sub/{fst}/{snd}")
async def calc_sub(fst:float, snd:float)->dict[str,float]:
    """API to sub two  numbers"""

    rst:float = sub(fst, snd)
    return {"result": rst}

@app.get("/calc/mul/{fst}/{snd}")
async def calc_sub(fst:float, snd:float)->dict[str,float]:
    """API to mul two  numbers"""

    rst:float = mul(fst, snd)
    return {"result": rst}

@app.get("/calc/operations/")
async def calc_operations()->dict[str,list[str]]:
    """API to get operations"""

    rst:list[str] = ["add", "mul", "sub"]
    return {"operations": rst}