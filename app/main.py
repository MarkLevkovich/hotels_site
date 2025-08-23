from fastapi import FastAPI
from app.bookings.router import router as router_bookings
app = FastAPI()

@app.get('/')
def hello() -> list:
    return {
        'Hello in my web-site!'
    }


app.include_router(router_bookings)