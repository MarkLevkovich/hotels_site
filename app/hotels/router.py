import asyncio
from datetime import date
from fastapi_cache.decorator import cache
from fastapi import APIRouter, HTTPException, status
from app.hotels.dao import HotelsDAO
from app.hotels.models import Hotel




router = APIRouter(prefix='/hotels', tags=['Hotels'])

@router.get('/{loc}')
@cache(expire=20)
async def get_hotels(loc: str, d_from: date, d_to: date):
    await asyncio.sleep(3)
    return await HotelsDAO.find_by_place(location=loc, date_from=d_from, date_to=d_to)

@router.get('/')
async def get_all(d_from: date, d_to: date):
    return await HotelsDAO.find_all(date_from=d_from, date_to=d_to)