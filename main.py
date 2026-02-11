from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db.database import Base, engine
from models import (
    Product,
    User, Cart, Order, Payment, Review
)
from routers.product import router
from routers.users import user_router
from routers.cart import cart_router
from routers.order import order_router
from routers.review import review_router
from routers.payment import payment_router

Base.metadata.create_all(bind=engine)

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://bloomher-frontend.vercel.app",
        "http://localhost:5500",
        "http://127.0.0.1:5500",
        "https://bloomher-backend.onrender.com"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def greet():
    return {"message": "Welcome to server. Visit /docs for API documentation."}

app.include_router(router)
app.include_router(user_router)
app.include_router(cart_router)
app.include_router(order_router)
app.include_router(review_router)
app.include_router(payment_router)


