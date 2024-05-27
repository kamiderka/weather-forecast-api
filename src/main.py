from fastapi import FastAPI
from forecast.router import forecast_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = ["http://localhost:5173", "https://weather-forecast-tn81.onrender.com"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(forecast_router)
