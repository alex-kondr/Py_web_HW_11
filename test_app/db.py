import configparser
from pathlib import Path

from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


path = Path(__file__).parent
config = configparser.ConfigParser()
config.read(path.joinpath("config.ini"))

db_url = config.get("DB", "url")
engine = create_engine(db_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Note(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    description = Column(String(250))
    done = Column(Boolean, default=False)
    

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
