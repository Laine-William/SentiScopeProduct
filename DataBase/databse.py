from Models.product_model import Base as ProductBase
from Models.review_model import Base as ReviewBase
from DataBase.connection import engine

def init_db():
    ProductBase.metadata.create_all(bind=engine)
    ReviewBase.metadata.create_all(bind=engine)