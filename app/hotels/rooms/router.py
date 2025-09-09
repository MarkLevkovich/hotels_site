from datetime import date

from app.hotels.rooms.dao import RoomsDAO
from app.hotels.router import router



@router.get('/{hotel_id}/rooms')
async def get_rooms(h_id: int, d_from: date ,d_to: date):
    return await RoomsDAO.show_rooms(hotel_id=h_id, date_from=d_from, date_to=d_to)
