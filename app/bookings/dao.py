from datetime import date
from app.database import async_session_maker
from sqlalchemy import select, and_, or_, func
from app.bookings.models import Bookings
from app.dao.base import BaseDAO
from app.hotels.models import Room


class BookingsDAO(BaseDAO):
    model = Bookings

    @classmethod
    async def add(cls, room_id: int, date_from: date, date_to: date):
        booked_rooms = select(Bookings).where(
            and_(
                Bookings.room_id==room_id,
                or_(
                    and_(
                        Bookings.date_from >= date_from,
                        Bookings.date_from <= date_to
                    ),and_(
                        Bookings.date_from <= date_from,
                        Bookings.date_to > date_from
                    )
                )
            )
        ).cte('booked_rooms')

        rooms_left = select(
            (Room.quantity - func.count(booked_rooms.room.id)).label('rooms_left')
        )
