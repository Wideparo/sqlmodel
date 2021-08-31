from fastapi import FastAPI

app = FastAPI()

@app.get('/books')
async def get_all_books():
    pass

@app.post('/books')
async def create_a_book():
    pass

@app.get('/book/{book_id}')
async def get_a_book(book_id:int):
    pass

@app.put('/book/{book_id}')
async def get_all_books(book_id:int):
    pass

@app.delete('/book/{book_id}')
async def delete_a_book(book_id:int):
    pass


