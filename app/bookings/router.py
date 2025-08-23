from fastapi import APIRouter, Depends, Form, Response, Request
from sqlalchemy import select, delete, update
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from app.bookings.models import Bookings
from app.bookings.dao import BookingsDAO



router = APIRouter(
    prefix='/bookings',
    tags=['Bookings']
)

@router.get('/')
async def get_bookings():
    return await BookingsDAO.find_one_or_none(room_id=45)
