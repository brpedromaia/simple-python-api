from repository import bookRepository
from domain.book import BookOrm
from domain.book import BookModel

def findAll(page,size,sort,orderby):
    print("svc")
    print(size)
    print(page)
    objBook = bookRepository.findAll(page,size,sort,orderby)
    return objBook

def find(id):
    print(id)
    objBook = bookRepository.findById(id)
    return objBook

def insert(book: BookModel):
    objBook=BookOrm(**book.dict())
    objBook = bookRepository.insert(objBook)
    return objBook

def delete(id):
    objBook = bookRepository.delete(id)
    return objBook

def update(book: BookModel):
    objBook = bookRepository.update(book)
    return objBook