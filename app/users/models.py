from sqlalchemy import JSON, Integer, String, Boolean, Column, ForeignKey, Date, Computed
from app.database import Base
from sqlalchemy.orm import relationship

class Users(Base):
    __tablename__='users'
    # __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)

    bookings = relationship('Bookings', back_populates='user')


    def __str__(self):
        return f'User #{self.email}'