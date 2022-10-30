from sqlalchemy import Column, Integer, String, Float

from db import Base


class TicketType(Base):
    __tablename__ = "ticket_types"

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    price = Column(Float, nullable=False)
