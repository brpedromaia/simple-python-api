from typing import List
from typing import Optional

from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from pydantic import BaseModel

class Base(DeclarativeBase):
    pass
    
class BookOrm(Base):
    __tablename__ = 'books'
    id: Mapped[str] = mapped_column(String(30),primary_key=True)
    name: Mapped[Optional[str]]
    author: Mapped[Optional[str]]
    publication_year: Mapped[Optional[int]]
    genre: Mapped[Optional[str]]
    def __repr__(self) -> str:
        return f"Book(id={self.id!r}, name={self.name!r}, author={self.author!r}, publication_year={self.publication_year!r}, genre={self.genre!r})"


 
class BookModel(BaseModel):
    id: str
    name: str
    author: str
    publication_year: int
    genre: str

    class Config:
        orm_mode = True


