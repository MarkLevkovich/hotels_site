from app.dao.base import BaseDAO
from app.hotels.models import Hotel
from app.database import async_session_maker
from sqlalchemy import select, delete, update
from sqlalchemy import select, func, or_, and_, not_
from datetime import date
from app.database import async_session_maker
from app.hotels.models import Hotel, Room
from app.bookings.models import Bookings as Booking

class HotelsDAO(BaseDAO):
    model = Hotel



    @classmethod
    async def find_by_place(cls, location: str, date_from: date, date_to: date):
        async with async_session_maker() as sm:
            available_rooms = (
                select(Room.id)
                .where(
                    Room.hotel_id==Hotel.id,
                    Room.id.not_in(
                        select(Booking.room_id)
                        .where(
                            or_(
                                and_(
                                    Booking.date_from < date_to,
                                    Booking.date_to > date_from
                                )
                            )
                        )
                    )
                )
                .exists()
            )

            condition = [
                Hotel.location.ilike(f"%{location}%"),
                available_rooms
            ]

            query = select(Hotel).where(*condition)
            result = await sm.execute(query)
            return result.scalars().all()








