import json
from fastapi import APIRouter, Response,Request
from services import bookService
from domain.book import BookModel
from typing import Dict,Optional

resource = APIRouter(prefix="/books",tags=["books"],)


@resource.get("/")
async def findAll(response:Response,page:Optional[int]=1,size: Optional[int]=2,sort: Optional[str] ='ASC',orderby: Optional[str] ='id'): 
    
    objBook = bookService.findAll(page,size,sort,orderby)
    
    if objBook is not None and len(objBook['result']) > 0:
        response.status_code = 200
        return objBook
    else:
        response.status_code = 404
        return "404 Not Found"


@resource.get("/{book_id}")
async def find(book_id, response: Response):
    
    objBook = bookService.find(book_id)
    
    if objBook is not None:
        response.status_code = 200
        return objBook
    else:
        response.status_code = 404
        return "404 Not Found"


@resource.post("/")
async def insert(book: BookModel, response: Response):
    
    objBook = bookService.find(book.id)
    
    if objBook is not None:
        response.status_code = 403
        return "403 Forbidden - Item already exists"

    objBook = bookService.insert(book)

    if objBook is not None:
        response.status_code = 201
        return "201 Created"
    else:
        response.status_code = 503
        return "503 Service Unavailable"


@resource.put("/")
async def update(book: BookModel, response: Response):
    
    objBook = bookService.find(book.id)
    
    if objBook is None:
        response.status_code = 404
        return "404 Not Found"

    objBook = bookService.update(book)
    
    if objBook is not None:
        response.status_code = 202
        return "202 Accepted"
    else:
        response.status_code = 503
        return "503 Service Unavailable"

@resource.delete("/{book_id}")
async def delete(book_id, response: Response):
    
    objBook = bookService.find(book_id)
    
    if objBook is None:
        response.status_code = 404
        return "404 Not Found"
    objBook = bookService.delete(book_id)
    
    if objBook is None:
        response.status_code = 202
        return "202 Accepted"
    else:
        response.status_code = 503
        return "503 Service Unavailable"