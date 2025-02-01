from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
 

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

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

# Start the Server ==> fastapi dev main.py   
