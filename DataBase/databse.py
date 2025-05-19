from Models.product import Base as ProductBase
from Models.review import Base as ReviewBase
from DataBase.connection import engine

def init_db():
    ProductBase.metadata.create_all(bind=engine)
    ReviewBase.metadata.create_all(bind=engine)