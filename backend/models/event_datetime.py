from sqlalchemy import Column, Integer, String

from db import Base


class EventDateTime(Base):
    __tablename__ = "event_datetimes"

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    datetime = Column(String, nullable=False)
    event_id = Column(Integer, nullable=False)
