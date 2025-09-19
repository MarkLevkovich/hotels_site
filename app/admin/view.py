from app.bookings.models import Bookings
from app.hotels.models import Room, Hotel
from app.users.models import Users
from sqladmin import ModelView




class UserAdmin(ModelView, model=Users):
    column_list = [Users.id, Users.email]
    column_details_exclude_list = [Users.hashed_password]
    can_delete = False
    name = 'User'
    name_plural = 'Users'
    icon = 'fa-solid fa-user'


class RoomsAdmin(ModelView, model=Room):
    column_list = [c.name for c in Room.__table__.c] + [Room.hotel, Room.bookings]
    name = 'Room'
    name_plural = 'Rooms'
    icon = 'fa-solid fa-bed'


class BookingsAdmin(ModelView, model=Bookings):
    column_list = [c.name for c in Bookings.__table__.c] + [Bookings.user, Bookings.room]
    name = 'Booking'
    name_plural = 'Bookings'
    icon = 'fa-solid fa-book'

class HotelAdmin(ModelView, model=Hotel):
    column_list = [c.name for c in Hotel.__table__.c] + [Hotel.rooms]
    name = 'Hotel'
    name_plural = 'Hotels'
    icon = 'fa-solid fa-hotel'