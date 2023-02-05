from db import get_db
from fastapi import APIRouter, Depends, HTTPException
from models.user import User
from sqlalchemy.orm import Session

from .errors import NotFound404

users_router = APIRouter(prefix='/users', tags=['users'])


@users_router.post("/create_user")
def create_user(name: str, phone: str, db: Session = Depends(get_db)):
    user_model = User()
    user_model.name = name
    user_model.phone = phone

    db.add(user_model)
    db.commit()

    # если возвращать user_model, ничего нормально не выведется
    # поэтому приходится запрашивать тот же объект из базы
    return get_user_by_id(user_model.id, db)


@users_router.get("/get_all_users")
def get_all_users(db: Session = Depends(get_db)):
    return db.query(User).all()


@users_router.get("/get_user_by_id")
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()

    if user is None:
        raise NotFound404(detail=f"User with ID {user_id} is not exist")

    return user


@users_router.get("/get_user_by_phone")
def get_user_by_phone(user_phone: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.phone == user_phone).first()

    if user is None:
        raise NotFound404(detail=f"User with Phone {user_phone} is not exist")

    return user


@users_router.delete("/delete_user_by_id")
def delete_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()

    if user is None:
        raise NotFound404(detail=f"User with ID {user_id} is not exist")

    db.query(User).filter(User.id == user_id).delete()
    db.commit()
