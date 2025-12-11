from pydantic import BaseModel
from typing import Optional

class BookCreate(BaseModel):
    title: str                     # название книги (обязательное поле)
    author: str                    # автор книги (обязательное поле)
    year: Optional[int] = None     # год издания (необязательное поле)

class BookRead(BookCreate):
    id: int

    class Config:
        orm_mode = True
