from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

db_url = "postgresql+psycopg2://postgres:AcademyRootPassword@localhost:5432/fullstack_project"

engine = create_engine(db_url)

SessionLocal = sessionmaker(autocommit=False, autoflush =False, bind=engine)

Base = declarative_base()



