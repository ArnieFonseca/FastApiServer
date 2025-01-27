from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
 

from routes.calculator import routerCalc
app = FastAPI()
app.include_router(routerCalc)

 
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

# Start the Server ==> fastapi dev main.py   
