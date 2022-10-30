from datetime import datetime as dt
from enum import Enum
from random import randint

from db import get_db
from fastapi import APIRouter, Depends, HTTPException
from models.order import Order
from models.user import User
from sqlalchemy.orm import Session
from .tickets import TicketTitle, get_ticket_type_by_title

from api.users import create_user

from .errors import NotFound404, WrongDateTimeFormat

orders_router = APIRouter(prefix='/orders', tags=['orders'])

datetime_format = "%Y-%m-%d %H:%M:%S"


#! Add times of tickets and direction
# ^ (A to B, B to A, A to B to A)


class EventDirection(str, Enum):
    AtoB = "Из A в B"
    BtoA = "Из B в A"
    AtoBtoA = "Из A в B и обратно в A"


@orders_router.post("/create_order")
def create_order(event_id: int,
                 event_datetime: str,
                 event_direction: EventDirection,
                 ticket_type_title: TicketTitle,
                 ticket_quantity: int,
                 user_name: str,
                 user_phone: str,
                 db: Session = Depends(get_db)):
    order_model = Order()
    order_model.event_id = event_id

    try:
        dt.strptime(event_datetime, datetime_format)
    except:
        raise WrongDateTimeFormat(
            f"Datetime {event_datetime} does not match format ({datetime_format})")

    order_model.event_datetime = event_datetime
    order_model.event_direction = event_direction

    ticket_type = get_ticket_type_by_title(ticket_type_title, db)
    order_model.ticket_type = ticket_type.title

    order_model.ticket_quantity = ticket_quantity

    barcode = randint(10000000, 99999999)
    order_model.barcode = barcode

    equal_price = float(ticket_type.price * ticket_quantity)

    user = db.query(User).filter(User.phone == user_phone).first()
    if user is None:
        user = create_user(user_name, user_phone, db)
    order_model.user_id = user.id

    order_model.equal_price = equal_price

    created = dt.now().strftime(datetime_format)
    order_model.created = created

    db.add(order_model)
    db.commit()

    # если возвращать order_model, ничего нормально не выведется
    # поэтому приходится запрашивать тот же объект из базы
    return get_order_by_id(order_model.id, db)


@orders_router.get("/get_all_orders")
def get_all_orders(db: Session = Depends(get_db)):
    return db.query(Order).all()


@orders_router.get("/get_order_by_id")
def get_order_by_id(order_id: int, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()

    if order is None:
        raise NotFound404(detail=f"Order with ID {order_id} is not exist")

    return order


@orders_router.get("/get_order_by_barcode")
def get_order_by_barcode(barcode: int, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.barcode == barcode).first()

    if order is None:
        raise NotFound404(detail=f"Order with Barcode {barcode} is not exist")

    return order


@orders_router.delete("/delete_order_by_id")
def delete_order_by_id(order_id: int, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()

    if order is None:
        raise NotFound404(detail=f"Order with ID {order_id} is not exist")

    db.query(Order).filter(Order.id == order_id).delete()
    db.commit()
