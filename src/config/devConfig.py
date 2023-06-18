from domain.book import BookOrm
from domain.book import Base
from repository import bookRepository
from sqlalchemy import create_engine
from sqlalchemy.orm import Session



def init():
  session = Session(getEngine())
  Base.metadata.create_all(getEngine())
  firstBook= BookOrm(id='B0001',name='The Hobbit',author='J. R. R. Tolkien',publication_year=1937,genre='Fantasy')
  secondBook= BookOrm(id='B0002',name='Harry Potter and the Philosopher\'s Stone',author='J. K. Rowling',publication_year=1997,genre='Fantasy')
  try:
    bookRepository.insert(firstBook)
    bookRepository.insert(secondBook)
  except:
    print("Mock data already inserted")


def getEngine():
  engine = create_engine("sqlite:///test.db", echo=True)
  return engine