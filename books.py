from fastapi import FastAPI,Path,status,Query
from src.modal.bookModel import Book, BookRequest
app = FastAPI()

BOOKS = [
    Book(1,"Harry Potter","J.K.Rowling","A great book", 5,2004),
    Book(2,"HP1","J.K.Rowling","A great book", 5,2001),
    Book(3,"HP2","J.K.Rowling","A great book", 5,2002),
    Book(4,"HP3","J.K.Rowling","A great book", 5,2003),
    Book(5,"HP4","J.K.Rowling","A great book", 5,1999),
]


# returns all the books through get function

@app.get("/book",status_code=status.HTTP_200_OK)
def get_all_books():
    return BOOKS

# returns books by the id passed as parameter to the route
@app.get("/book/{book_id}",status_code=status.HTTP_200_OK)
def get_book_by_id(book_id:int=Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book



# returns book by query param passed on the router
@app.get("/book/",status_code=status.HTTP_200_OK)
def get_book(rating:int= None and Query(gt=0,lt=6), published_date:int= None and Query(gt=1999,lt=2040)):
    books = []
    for book in BOOKS:
        if published_date is not None and book.published_date!=published_date:
            continue
        if rating is not None and book.rating!=rating:
            continue
        books.append(book)
    return books




# user passes data through thr body and it gets stored on out data list. We have used "BookRequest" type created through pydantic package.
@app.post("/book",status_code=status.HTTP_201_CREATED)
def create_book(book:BookRequest):
    new_book = Book(**book.model_dump())
    BOOKS.append(get_book_id(new_book))

def get_book_id(book:BookRequest):
    book.id = 1 if len(BOOKS)==0 else BOOKS[-1].id+1
    return book

# user passes the proper updated value in the body , based on the bosy the put route automatically updates the record in out list
@app.put("/book/",status_code=status.HTTP_204_NO_CONTENT)
def put_book(newBook: BookRequest):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == newBook.id:
            BOOKS[i]= newBook
            break

# user passes the proper updated value in the body , based on the bosy the put route automatically updates the record in out list
@app.delete("/book/{book_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id:int=Path(gt=0)):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            break
