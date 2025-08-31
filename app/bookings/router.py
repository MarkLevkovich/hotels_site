from datetime import date

from fastapi import APIRouter, Depends, Form, Response, Request
from sqlalchemy import select, delete, update
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from app.bookings.models import Bookings
from app.bookings.dao import BookingsDAO
from app.bookings.schemas import SBookings
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix='/bookings',
    tags=['Bookings']
)

@router.get('/')
async def get_bookings(user: Users = Depends(get_current_user)):
    return await BookingsDAO.find_all(user_id=user.id)

@router.post('/')
async def add_bookings(room_id: int, date_from: date, date_to: date, user: Users = Depends(get_current_user)):
    await BookingsDAO.add(user.id, room_id, date_from, date_to)

