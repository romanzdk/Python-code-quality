from fastapi import FastAPI, HTTPException, Depends, Query
from pydantic import BaseModel, Field
from typing import List, Optional
from uuid import UUID, uuid4
from datetime import date

app = FastAPI()

class Author(BaseModel):
    name: str
    birth_date: Optional[date] = None

class Book(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    title: str
    author: Author
    publication_date: date
    pages: int

class BookCreate(BaseModel):
    title: str
    author: Author
    publication_date: date
    pages: int

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[Author] = None
    publication_date: Optional[date] = None
    pages: Optional[int] = None

example_book = Book(
	title='Book title',
	author = Author(name='Author Name'),
	publication_date = date(2024,2,11),
	pages = 360
)

books_db: List[Book] = [example_book]

def get_db():
    return books_db

@app.get("/books/", response_model=List[Book])
async def read_books(skip: int = 0, limit: int = 10, db: List[Book] = Depends(get_db)):
    return db[skip : skip + limit]

@app.get("/books/{book_id}", response_model=Book)
async def read_book(book_id: UUID, db: List[Book] = Depends(get_db)):
    for book in db:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.post("/books/", response_model=Book, status_code=201)
async def create_book(book: BookCreate, db: List[Book] = Depends(get_db)):
    new_book = Book(**book.dict())
    db.append(new_book)
    return new_book

@app.put("/books/{book_id}", response_model=Book)
async def update_book(book_id: UUID, book_update: BookUpdate, db: List[Book] = Depends(get_db)):
    for idx, book in enumerate(db):
        if book.id == book_id:
            updated_book_data = book.copy(update=book_update.dict(exclude_unset=True))
            db[idx] = updated_book_data
            return updated_book_data
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{book_id}", status_code=204)
async def delete_book(book_id: UUID, db: List[Book] = Depends(get_db)):
    for idx, book in enumerate(db):
        if book.id == book_id:
            del db[idx]
            return
    raise HTTPException(status_code=404, detail="Book not found")

@app.get("/books/search/", response_model=List[Book])
async def search_books(title: Optional[str] = Query(None, min_length=3), db: List[Book] = Depends(get_db)):
    if title:
        return [book for book in db if title.lower() in book.title.lower()]
    return db
