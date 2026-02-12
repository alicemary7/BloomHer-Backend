import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Get DB URL from environment variables for Render deployment
# Fallback to the hardcoded URL for local testing if needed
db_url = os.environ.get("DATABASE_URL")
if not db_url:
    db_url = "postgresql://e_commerce_website_m16e_user:6KBd02SB5rfwe701VH2YaSJOCtUMzfE5@dpg-d5scavi4d50c73d9f9o0-a.virginia-postgres.render.com/e_commerce_website_m16e"

# Fix for Render/Heroku: update URLs starting with postgres:// to postgresql://
if db_url and db_url.startswith("postgres://"):
    db_url = db_url.replace("postgres://", "postgresql://", 1)

engine = create_engine(db_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()



