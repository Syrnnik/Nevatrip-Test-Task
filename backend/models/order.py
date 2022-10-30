from sqlalchemy import Column, Integer, DateTime, Float, String

from db import Base


# * Orders table

class Order(Base):
    __tablename__ = "phpMyAdmin"

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    event_id = Column(Integer, nullable=False)
    event_datetime = Column(String, nullable=False)
    event_direction = Column(String, nullable=False)
    ticket_type = Column(String, nullable=False)
    ticket_quantity = Column(Integer, nullable=False)
    barcode = Column(String, nullable=False)
    user_id = Column(Integer, nullable=False)
    equal_price = Column(Float, nullable=False)
    created = Column(String, nullable=False)
