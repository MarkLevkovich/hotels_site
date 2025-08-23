from app.database import async_session_maker
from sqlalchemy import select
from app.bookings.models import Bookings
from app.dao.base import BaseDAO

class BookingsDAO(BaseDAO):
    model = Bookings 
