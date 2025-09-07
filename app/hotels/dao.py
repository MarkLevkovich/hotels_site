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
    async def find_available_hotels(
            cls,
            location: str,
            date_from: date,
            date_to: date,
            **additional_filters
    ):
        """
        Корректный поиск отелей со свободными комнатами
        """
        async with async_session_maker() as session:
            # Подзапрос для поиска свободных комнат в отеле
            available_rooms_subquery = (
                select(Room.id)
                .where(
                    Room.hotel_id == Hotel.id,
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

            conditions = [
                Hotel.location.ilike(f"%{location}%"),
                available_rooms_subquery  # Есть хотя бы одна свободная комната
            ]

            for key, value in additional_filters.items():
                conditions.append(getattr(Hotel, key) == value)

            query = select(Hotel).where(*conditions)
            result = await session.execute(query)
            return result.scalars().all()