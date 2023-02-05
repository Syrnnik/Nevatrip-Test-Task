from enum import Enum

from db import get_db
from fastapi import APIRouter, Depends, HTTPException
from models.event_datetime import EventDateTime
from sqlalchemy.orm import Session

from .errors import NotFound404

event_datetimes_router = APIRouter(
    prefix='/event_datetimes', tags=['event_datetimes'])


@event_datetimes_router.post("/")
def create_event_datetimetable(event_id: int,
                               event_datetime: str,
                               db: Session = Depends(get_db)):
    event_datetime_model = EventDateTime()
    event_datetime_model.datetime = event_datetime
    event_datetime_model.event_id = event_id

    db.add(event_datetime_model)
    db.commit()

    # если возвращать event_datetime_model, ничего нормально не выведется
    # поэтому приходится запрашивать тот же объект из базы
    return get_event_datetime_by_id(event_datetime_model.id, db)


@event_datetimes_router.get("/")
def get_all_event_datetimes(db: Session = Depends(get_db)):
    return db.query(EventDateTime).all()


@event_datetimes_router.get("/{event_datetime_id}")
def get_event_datetime_by_id(event_datetime_id: int, db: Session = Depends(get_db)):
    event_datetime = db.query(EventDateTime).filter(
        EventDateTime.id == event_datetime_id).first()

    if event_datetime is None:
        raise NotFound404(
            detail=f"EventDateTime with ID {event_datetime_id} is not exist")

    return event_datetime


@event_datetimes_router.get("/events/{event_id}")
def get_event_datetimes_by_event_id(event_id: int, db: Session = Depends(get_db)):
    event_datetimes = db.query(EventDateTime).filter(
        EventDateTime.event_id == event_id).all()

    if event_datetimes is None:
        raise NotFound404(
            detail=f"EventDateTime with EventID {event_id} is not exist")

    return event_datetimes


@event_datetimes_router.put("/{event_datetime_id}")
def update_event_datetime_by_id(event_datetime_id: int,
                                event_datetime: str,
                                event_id: int,
                                db: Session = Depends(get_db)):

    event_datetime_model = db.query(EventDateTime).filter(
        EventDateTime.id == event_datetime_id).first()

    if event_datetime_model is None:
        raise NotFound404(
            detail=f"EventDateTime with ID {event_datetime_id} is not exist")

    event_datetime_model.event_datetime = event_datetime
    event_datetime_model.event_id = event_id

    db.add(event_datetime_model)
    db.commit()

    # если возвращать event_datetime_model, ничего нормально не выведется
    # поэтому приходится запрашивать тот же объект из базы
    return get_event_datetime_by_id(event_datetime_model.id, db)


@event_datetimes_router.delete("/{event_datetime_id}")
def delete_event_datetime_by_id(event_datetime_id: int, db: Session = Depends(get_db)):
    event_datetime = db.query(EventDateTime).filter(
        EventDateTime.id == event_datetime_id).first()

    if event_datetime is None:
        raise NotFound404(
            detail=f"EventDateTime with ID {event_datetime_id} is not exist")

    db.query(EventDateTime).filter(
        EventDateTime.id == event_datetime_id).delete()
    db.commit()
