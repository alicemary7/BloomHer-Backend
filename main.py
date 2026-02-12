from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
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

print("Connecting to database...")
try:
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully (if they didn't exist).")
except Exception as e:
    print(f"Error creating tables: {e}")

app=FastAPI()

with engine.connect() as conn:
    print("Checking for missing columns...")
    try:
        # Add missing columns if they don't exist
        conn.execute(text("ALTER TABLE products ADD COLUMN IF NOT EXISTS price_small FLOAT"))
        conn.execute(text("ALTER TABLE products ADD COLUMN IF NOT EXISTS price_regular FLOAT"))
        conn.execute(text("ALTER TABLE products ADD COLUMN IF NOT EXISTS price_large FLOAT"))
        conn.execute(text("ALTER TABLE products ADD COLUMN IF NOT EXISTS price_xl FLOAT"))
        conn.execute(text("ALTER TABLE products ADD COLUMN IF NOT EXISTS rating FLOAT DEFAULT 0"))
        conn.execute(text("ALTER TABLE products ADD COLUMN IF NOT EXISTS review_count INTEGER DEFAULT 0"))
        conn.execute(text("ALTER TABLE products ADD COLUMN IF NOT EXISTS features TEXT"))
        conn.commit()
        print("Schema update check completed.")
    except Exception as e:
        print(f"Error updating schema: {e}")

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
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
