from sqlalchemy import Column, Integer, String, Text, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from .database import Base

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    user_name = Column(String, nullable=True)
    comment_text = Column(Text)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    sentiment_compound_score = Column(Float)
    
    product = relationship("Product", back_populates="reviews") 