from fastapi import FastAPI, Body

app = FastAPI()


BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Six', 'category': 'math'},
    {'title': 'Title Seven', 'author': 'Author Seven', 'category': 'science'}
]

# GET req method

# 127.0.0.1:8000/
@app.get("/")
async def first_api():
    return {'message':  'Hello Welcome'}

# Path Parameters

@app.get("/books")
async def get_all_book():
    return BOOKS

@app.get("/books/{book_title}")
async def read_all_books(book_title: str):
    if BOOKS:
        for book in BOOKS:
            if book.get('title').casefold() == book_title.casefold():
                return book
        return {"No Books": "Books are Not Matching"}
    else:
        return {"No Books": "Books are empty"}

# Query Parameters

@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

@app.get("/books/{author_name}/")
async def get_book_by_author_and_cat(author_name: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold() and \
            book.get('author').casefold() == author_name.casefold():
            books_to_return.append(book)
    return books_to_return

# POST req method
@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)


# PUT req method
@app.put("/books/updated_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book

# DELETE req method
@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break







