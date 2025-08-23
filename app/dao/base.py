from app.database import async_session_maker
from sqlalchemy import select
from app.bookings.models import Bookings


class BaseDAO():
    model = None

    @classmethod #обращение к функции без экземпляра класса
    async def find_all(cls):
        async with async_session_maker() as session:
            query = select(cls.model)
            result = await session.execute(query)
            return result.scalars().all()