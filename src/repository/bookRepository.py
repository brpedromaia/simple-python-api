from sqlalchemy import select, text
from sqlalchemy.orm import Session
from domain.book import BookOrm
from domain.book import BookModel
from config import appConfig


def findAll(page,size,sort,orderby):
    session = Session(appConfig.getEngine())
    page=(page-1)
    t_rows=session.query(BookOrm).count()
    t_pages=int(((t_rows + size - 1) / size))
    result_query = session.query(BookOrm).order_by(text(orderby+" "+sort)).limit(size).offset(page*size).all()
    session.close()
    result:Dict = {
        "metadata": {
            "pageSize": size,
            "currentPage": page,
            "totalPages": t_pages,
            "totalRecord": t_rows,
            "orderby": orderby,
            "sort": sort
        },
        "result": []
        }
    result['result']=result_query
    return result

def findById(id):
    session = Session(appConfig.getEngine())
    stmt = (select(BookOrm).where(BookOrm.id == id))
    result = session.scalars(stmt).one_or_none() 
    session.close()
    return result

def insert(book: BookOrm):
    session = Session(appConfig.getEngine())
    session.add(book)
    session.commit()
    session.refresh(book)
    session.close()
    return book

def delete(id):
    session = Session(appConfig.getEngine())
    obj=findById(id)
    session.delete(obj)
    session.commit()
    session.close()

def update(book: BookModel):
    session = Session(appConfig.getEngine())
    session.query(BookOrm).filter(BookOrm.id == book.id).update(book.dict(), synchronize_session = False)
    session.commit()
    session.close()
    return book