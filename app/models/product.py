from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship

from .database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text)
    
    reviews = relationship("Review", back_populates="product", cascade="all, delete-orphan")