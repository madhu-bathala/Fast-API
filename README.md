# FastAPI Notes
## Installations
pip install fastapi <br>
pip install uvicorn <br>
pip install uvicorn["standards"] <br>
## HTTP Methods
CREATE -- POST <br>
READ -- GET <br>
UPDATE -- PUT <br>
DELETE -- DELETE <br>
## Runserver
local -- uvicorn file_name:app --reload <br>
dev   -- fastapi dev file_name.py <br>
prod  -- fastapi run file_name.py <br>
## Path Parameters
@app.get("/books") <br>
@app.get("/books/{dynamic_parameter}") <br>
## Query Parameter
@app.get("/books/?category=math") <br>
## Request Methods
@app.get("/books") -- get all books <br>
@app.get("/books/{book_title}") -- get books by title <br>
@app.post("/books/create_book") -- create new book <br>
@app.put("/books/update_book") -- update book <br>
@app.delete("/books/{book_id}") -- delete book by id <br>
@app.delete("/books/delete_book/{book_title}") -- delete book by book title <br>
## Status Codes
1xx --> Informal <br>
2xx --> Success <br>
3xx --> Redirection <br>
4xx --> Client Errors <br>
5xx --> Server Errors <br>







