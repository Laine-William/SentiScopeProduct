from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    user_name = Column(String, nullable=True)
    comment_text = Column(String, nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    sentiment_compound_score = Column(Float, nullable=False)