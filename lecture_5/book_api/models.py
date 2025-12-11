# models.py: определение модели Book
from sqlalchemy import Column, Integer, String
from database import Base  # импорт базового класса из database.py

class Book(Base):
    __tablename__ = "books"  # имя таблицы в БД
    id = Column(Integer, primary_key=True, index=True)        # уникальный идентификатор книги
    title = Column(String, index=True, nullable=False)        # название книги, обязательное поле
    author = Column(String, index=True, nullable=False)       # автор книги, обязательное поле
    year = Column(Integer, nullable=True)                     # год издания, необязательное поле
