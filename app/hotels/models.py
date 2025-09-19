from app.database import Base
from sqlalchemy import Column, Integer, String, Boolean, JSON, ForeignKey
from sqlalchemy.orm import relationship


class Hotel(Base):
    __tablename__ = 'hotels'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    services = Column(JSON)
    rooms_quantity = Column(Integer, nullable=False)
    image_id = Column(Integer)

    rooms = relationship('Room', back_populates='hotel')

    def __str__(self):
        return f'Hotel #{self.name}, location -> {self.location[:30]}'


class Room(Base):
    __tablename__ = 'rooms'
    id = Column(Integer, primary_key=True)
    hotel_id = Column(Integer, ForeignKey('hotels.id'), nullable=False)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Integer, nullable=False)
    services = Column(JSON)
    quantity = Column(Integer)
    image_id = Column(Integer)

    bookings = relationship('Bookings', back_populates='room')
    hotel = relationship('Hotel', back_populates='rooms')

    def __str__(self):
        return f'Room #{self.id}'