from app.hotels.rooms.dao import RoomsDAO
from app.hotels.router import router



@router.get('/{hotel_id}/rooms')
async def get_rooms(h_id: int):
    return await RoomsDAO.show_rooms(hotel_id=h_id)
