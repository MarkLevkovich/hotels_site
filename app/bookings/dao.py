from datetime import date
from app.database import async_session_maker
from sqlalchemy import select, and_, or_, func
from app.bookings.models import Bookings
from app.dao.base import BaseDAO
from app.hotels.models import Room


class BookingsDAO(BaseDAO):
    model = Bookings

    @classmethod
    async def add(cls, user_id: int, room_id: int, date_from: date, date_to: date):
        async with async_session_maker() as session:
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
                    (Room.quantity - func.count(booked_rooms.c.room_id)).label('rooms_left')
                    ).select_from(Room).join(
                        booked_rooms, booked_rooms.c.room_id == Room.id
                    ).where(Room.id==room_id).group_by(
                        Room.quantity, booked_rooms.c.room_id
                    )
                rooms_left = await session.execute(rooms_left)
                print(rooms_left.scalar())
