from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional

import models, schemas
from database import engine, Base, get_db

app = FastAPI()

Base.metadata.create_all(bind=engine)  # создаёт таблицы по описанным моделям

@app.post("/books/", response_model=schemas.BookRead)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):

    db_book = models.Book(title=book.title, author=book.author, year=book.year)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)  # обновляем объект, чтобы получить сгенерированный ID
    return db_book

@app.get("/books/", response_model=list[schemas.BookRead])
def read_books(title: Optional[str] = None, db: Session = Depends(get_db)):

    if title:
        # Поиск книг, название которых содержит подстроку title
        return db.query(models.Book).filter(models.Book.title.contains(title)).all()
    return db.query(models.Book).all()

@app.get("/books/{book_id}", response_model=schemas.BookRead)
def read_book(book_id: int, db: Session = Depends(get_db)):

    book = db.query(models.Book).get(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.put("/books/{book_id}", response_model=schemas.BookRead)
def update_book(book_id: int, book_data: schemas.BookCreate, db: Session = Depends(get_db)):

    book = db.query(models.Book).get(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    book.title = book_data.title
    book.author = book_data.author
    book.year = book_data.year
    db.commit()
    db.refresh(book)
    return book

@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):

    book = db.query(models.Book).get(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    return {"message": "Book deleted successfully"}
