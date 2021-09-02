from fastapi import FastAPI
from fastapi import status
from fastapi.exceptions import HTTPException
from database import engine
from models import Book
from sqlmodel import Session, select
from typing import Optional, List

app = FastAPI()
session = Session(bind=engine)


@app.get('/book', response_model=List[Book], status_code=status.HTTP_200_OK)
async def get_all_books():
    statement = select(Book)
    results = session.exec(statement).all()

    return results


@app.post('/books')
async def create_a_book():
    pass


@app.get('/book/{book_id}', response_model=Book)
async def get_all_books(book_id: int):
    statement = select(Book).where(Book.id == book_id)
    result = session.exec(statement).first()
    if result == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return result


@app.put('/book/{book_id}')
async def get_all_books(book_id: int):
    pass


@app.delete('/book/{book_id}')
async def delete_a_book(book_id: int):
    pass
