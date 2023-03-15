from typing import List

from sqlalchemy.orm import Session

from src.database.models import Contact
from src.schemas.contacts import ContactModel


async def get_contacts(skip: int, limit: int, db: Session) -> List[Contact]:
    return db.query(Contact).offset(skip).limit(limit).all()


async def create_contact(body: ContactModel, db: Session) -> Contact:
    contact = Contact(**vars(body))
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact