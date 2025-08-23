from fastapi import APIRouter, Depends, Form, Response, Request
from sqlalchemy import select, delete, update
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from app.bookings.models import Bookings
from app.bookings.dao import BookingsDAO
from app.bookings.schemas import SBookings


router = APIRouter(
    prefix='/bookings',
    tags=['Bookings']
)

@router.get('/')
async def get_bookings() -> list[SBookings]:
    return await BookingsDAO.find_all()
