import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Base
from config.env import env

DATABASE_URL = (
    f"postgresql://{env.POSTGRES_USER.value}:"
    f"{env.POSTGRES_PASSWORD.value}@"
    f"{env.POSTGRES_HOST.value}:{env.POSTGRES_PORT.value}/"
    f"{env.POSTGRES_DB.value}"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()