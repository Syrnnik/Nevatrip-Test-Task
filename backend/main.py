from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn


from api.users import users_router
from api.tickets import tickets_router
from api.events import events_router
# from api.event_datetimes import event_datetimes_router
from api.orders import orders_router

from db import Base, engine


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_router)
app.include_router(tickets_router)
app.include_router(events_router)
# app.include_router(event_datetimes_router)
app.include_router(orders_router)

Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    uvicorn.run("main:app", host='localhost',
                debug=True, reload=True, workers=1)
