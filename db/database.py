from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

db_url = "postgresql://e_commerce_website_m16e_user:6KBd02SB5rfwe701VH2YaSJOCtUMzfE5@dpg-d5scavi4d50c73d9f9o0-a.virginia-postgres.render.com/e_commerce_website_m16e"

engine = create_engine(db_url)

SessionLocal = sessionmaker(autocommit=False, autoflush =False, bind=engine)

Base = declarative_base()



