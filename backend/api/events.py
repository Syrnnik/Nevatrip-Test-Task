from db import get_db
from fastapi import APIRouter, Depends, HTTPException
from models.event import Event
from sqlalchemy.orm import Session

from .errors import NotFound404

events_router = APIRouter(prefix='/events', tags=['events'])


@events_router.post("/create_event")
def create_event(title: str, desc: str, duration: str, db: Session = Depends(get_db)):
    event_model = Event()
    event_model.title = title
    event_model.desc = desc
    event_model.duration = duration

    db.add(event_model)
    db.commit()

    # если возвращать event_model, ничего нормально не выведется
    # поэтому приходится запрашивать тот же объект из базы
    return get_event_by_id(event_model.id, db)


@events_router.get("/get_all_events")
def get_all_events(db: Session = Depends(get_db)):
    return db.query(Event).all()


@events_router.get("/get_event_by_id")
def get_event_by_id(event_id: int, db: Session = Depends(get_db)):
    event = db.query(Event).filter(Event.id == event_id).first()

    if event is None:
        raise NotFound404(detail=f"Event with ID {event_id} is not exist")

    return event


@events_router.put("/update_event_by_id")
def update_event_by_id(event_id: int, title: str, desc: str, duration: str, db: Session = Depends(get_db)):
    event_model = db.query(Event).filter(Event.id == event_id).first()

    if event_model is None:
        raise NotFound404(
            detail=f"Event with ID {event_id} is not exist")

    event_model.title = title
    event_model.desc = desc
    event_model.duration = duration

    db.add(event_model)
    db.commit()

    # если возвращать event_model, ничего нормально не выведется
    # поэтому приходится запрашивать тот же объект из базы
    return get_event_by_id(event_model.id, db)


@events_router.delete("/delete_event_by_id")
def delete_event_by_id(event_id: int, db: Session = Depends(get_db)):
    event = db.query(Event).filter(Event.id == event_id).first()

    if event is None:
        raise NotFound404(detail=f"Event with ID {event_id} is not exist")

    db.query(Event).filter(Event.id == event_id).delete()
    db.commit()
