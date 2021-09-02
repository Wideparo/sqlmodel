from  sqlmodel import SQLModel
from models import Book
from database import engine

print('Creating database.......')
SQLModel.metadata.create_all(engine)