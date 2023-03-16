from sqlalchemy import Column, Integer, String, func
from sqlalchemy.sql.sqltypes import Date, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Contact(Base):
    
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    phone = Column(String(18), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True, index=True)
    birthday = Column(Date)
    create_at = Column(DateTime, default=func.now())