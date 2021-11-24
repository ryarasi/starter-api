from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

POSTGRES_DB = str(os.getenv('POSTGRES_DB','db'))
POSTGRES_USER = str(os.getenv('POSTGRES_USER','user'))
POSTGRES_PASSWORD = str(os.getenv('POSTGRES_PASSWORD','password'))

SQLALCHEMY_DATABASE_URL = "postgresql://" + POSTGRES_USER + ":" + POSTGRES_PASSWORD + "@db:5432/" + POSTGRES_DB

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()