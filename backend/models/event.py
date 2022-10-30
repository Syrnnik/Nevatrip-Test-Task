from sqlalchemy import Column, Integer, String

from db import Base


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    desc = Column(String, nullable=False)
    duration = Column(String, nullable=False)
