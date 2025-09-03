from fastapi import FastAPI
from app.bookings.router import router as router_bookings
from app.users.router import router as router_users

app = FastAPI()

@app.get('/')
def hello() -> str:
    return 'Hello in my web-site!'


app.include_router(router_users)
app.include_router(router_bookings)


# https://www.canva.com/design/DAGx8IbwuWk/4pcQFnR1H_HfGgfjIxoFaQ/view?utm_content=DAGx8IbwuWk&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h3dd5ee65c5