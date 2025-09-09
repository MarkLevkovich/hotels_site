from app.bookings.models import Bookings
from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.hotels.models import Room
from sqlalchemy import select, insert, delete



class RoomsDAO(BaseDAO):
    model = Room

    @classmethod
    async def show_rooms(cls, hotel_id: int):
        async with async_session_maker() as session:
            query = select(Room).where(Room.hotel_id==hotel_id)
            res = await session.execute(query)
            return res.scalars().all()