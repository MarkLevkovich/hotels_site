from fastapi import FastAPI

from app.admin.auth import authentication_backend
from app.admin.view import UserAdmin, BookingsAdmin, RoomsAdmin, HotelAdmin
from app.bookings.router import router as router_bookings
from app.database import engine
from app.users.models import Users
from app.users.router import router as router_users
from app.hotels.router import router as router_hotels
from app.hotels.rooms.router import router as router_rooms
from app.pages.router import router as router_pages
from app.images.router import router as router_images
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from starlette.requests import Request
from starlette.responses import Response
from sqladmin import Admin, ModelView
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache

from redis import asyncio as aioredis


app = FastAPI()
app.mount('/static', StaticFiles(directory='app/static'), 'static')




origins = [
    'http://localhost:8000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "DELETE", "OPTIONS", "PUT", "PATCH",],
    allow_headers=["*"]


)

@app.get('/')
async def main_hello():
    return RedirectResponse(url='/pages/')


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url("redis://localhost:6379", encoding='utf8', decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix='cache')


#adminka
admin = Admin(app, engine, authentication_backend=authentication_backend)


admin.add_view(HotelAdmin)
admin.add_view(RoomsAdmin)
admin.add_view(UserAdmin)
admin.add_view(BookingsAdmin)




#routers
app.include_router(router_users)
app.include_router(router_bookings)
app.include_router(router_hotels)
app.include_router(router_rooms)
app.include_router(router_pages)
app.include_router(router_images)



