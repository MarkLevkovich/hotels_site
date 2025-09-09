from datetime import date

from app.bookings.models import Bookings
from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.hotels.models import Room
from sqlalchemy import select, insert, delete, and_, or_, func
from app.bookings.models import Bookings as Booking


class RoomsDAO(BaseDAO):
    model = Room

    @classmethod
    async def show_rooms(cls, hotel_id: int, date_from: date ,date_to: date):
        async with async_session_maker() as session:
            booked_rooms = (
                select(Bookings.room_id)
                .where(
                    and_(
                        Bookings.date_from <= date_to,
                        Booking.date_to >= date_from
                    )
                )
                .scalar_subquery()
            )

            available_rooms = select(Room).where(Room.hotel_id==hotel_id, Room.id.not_in(booked_rooms))

            result = await session.execute(available_rooms)
            return result.scalars().all()
