from datetime import date

from fastapi import APIRouter, HTTPException, status
from app.hotels.dao import HotelsDAO
from app.hotels.models import Hotel




router = APIRouter(prefix='/hotels', tags=['Hotels'])

@router.get('/{loc}')
async def get_hotels(loc: str, d_from: date, d_to: date):
    return await HotelsDAO.find_by_place(location=loc, date_from=d_from, date_to=d_to)

@router.get('/')
async def get_all(d_from: date, d_to: date):
    return await HotelsDAO.find_all(date_from=d_from, date_to=d_to)