"""Entry Pointy for the Fast API Service"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from routes.calculator import routerCalc
app = FastAPI()
app.include_router(routerCalc) 

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # Allow Any Domain
    allow_credentials=True,     # Allows cookies and authentication headers
    allow_methods=["*"],        # Allows all HTTP methods
    allow_headers=["*"],        # Allows all headers
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

# Start the Server ==> fastapi dev main.py   
