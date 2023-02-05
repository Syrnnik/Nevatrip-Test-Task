from enum import Enum

from db import get_db
from fastapi import APIRouter, Depends
from models.ticket_type import TicketType
from sqlalchemy.orm import Session

from .errors import NotFound404

tickets_router = APIRouter(prefix='/tickets_types', tags=['tickets_types'])


class TicketTitle(str, Enum):
    adult = "Взрослый"
    child = "Детский"
    preferential = "Льготный"
    group = "Групповой"


@tickets_router.post("/create_ticket_type")
def create_ticket_type(title: TicketTitle, price: float, db: Session = Depends(get_db)):
    ticket_type_model = TicketType()
    ticket_type_model.title = title
    ticket_type_model.price = price

    db.add(ticket_type_model)
    db.commit()

    # если возвращать ticket_type_model, ничего нормально не выведется
    # поэтому приходится запрашивать тот же объект из базы
    return get_ticket_type_by_id(ticket_type_model.id, db)


@tickets_router.get("/get_all_ticket_types")
def get_all_ticket_types(db: Session = Depends(get_db)):
    return db.query(TicketType).all()


@tickets_router.get("/get_ticket_type_by_id")
def get_ticket_type_by_id(ticket_type_id: int, db: Session = Depends(get_db)):
    ticket_type = db.query(TicketType).filter(
        TicketType.id == ticket_type_id).first()

    if ticket_type is None:
        raise NotFound404(
            detail=f"TicketType with ID {ticket_type_id} is not exist")

    return ticket_type


@tickets_router.get("/get_ticket_type_by_title")
def get_ticket_type_by_title(ticket_type_title: int, db: Session = Depends(get_db)):
    ticket_type = db.query(TicketType).filter(
        TicketType.title == ticket_type_title).first()

    if ticket_type is None:
        raise NotFound404(
            detail=f"TicketType with Title {ticket_type_title} is not exist")

    return ticket_type


@tickets_router.put("/update_ticket_by_id")
def update_ticket_by_id(ticket_type_id: int,
                        title: TicketTitle,
                        price: float,
                        db: Session = Depends(get_db)):
    ticket_model = db.query(TicketType).filter(
        TicketType.id == ticket_type_id).first()

    if ticket_model is None:
        raise NotFound404(
            detail=f"TicketType with ID {ticket_type_id} is not exist")

    ticket_model.title = title
    ticket_model.price = price

    db.add(ticket_model)
    db.commit()

    # если возвращать ticket_type_model, ничего нормально не выведется
    # поэтому приходится запрашивать тот же объект из базы
    return get_ticket_type_by_id(ticket_model.id, db)


@tickets_router.delete("/delete_ticket_type_by_id")
def delete_ticket_type_by_id(ticket_type_id: int, db: Session = Depends(get_db)):
    ticket_type = db.query(TicketType).filter(
        TicketType.id == ticket_type_id).first()

    if ticket_type is None:
        raise NotFound404(
            detail=f"TicketType with ID {ticket_type_id} is not exist")

    db.query(TicketType).filter(TicketType.id == ticket_type_id).delete()
    db.commit()
