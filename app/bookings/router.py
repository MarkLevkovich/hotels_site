from datetime import date
from fastapi import APIRouter, Depends, Form, Response, Request
from sqlalchemy import select, delete, update
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from app.bookings.models import Bookings
from app.bookings.dao import BookingsDAO
from app.bookings.schemas import SBookings
from app.tasks.tasks import send_booking_confirmation
from app.users.dependencies import get_current_user
from app.users.models import Users
from app.exeptions import NoRoomException, NoBookingException

router = APIRouter(
    prefix='/bookings',
    tags=['Bookings']
)

@router.get('/')
async def get_bookings(user: Users = Depends(get_current_user)):
    return await BookingsDAO.find_all(user_id=user.id)


@router.post('/add_booking')
async def add_bookings(
        room_id: int,
        date_from: date,
        date_to: date,
        user: Users = Depends(get_current_user)
):
    booking = await BookingsDAO.add(user.id, room_id, date_from, date_to)
    if not booking:
        raise NoRoomException
    else:

        booking_dict = {
            "id": booking.id,
            "user_id": booking.user_id,
            "room_id": booking.room_id,
            "date_from": booking.date_from.isoformat(),
            "date_to": booking.date_to.isoformat(),
            "price": float(booking.price) if booking.price else 0.0,
            "total_cost": booking.total_price,
            "total_days": booking.total_days

        }
        send_booking_confirmation.delay(booking_dict, user.email)
        return booking

@router.get('/del')
async def del_bookings(b_id: int, user: Users = Depends(get_current_user)):
    await BookingsDAO.delete_bookings(user.id, b_id)


