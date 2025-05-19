from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

# Schémas pour les produits
class ProductBase(BaseModel):
    name: str
    description: str

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True

# Schémas pour les commentaires
class ReviewBase(BaseModel):
    product_id: int
    user_name: Optional[str] = None
    comment_text: str

class ReviewCreate(ReviewBase):
    pass

class Review(ReviewBase):
    id: int
    timestamp: datetime
    sentiment_compound_score: float

    class Config:
        orm_mode = True

# Schéma pour le résumé des sentiments
class SentimentSummary(BaseModel):
    product_id: int
    product_name: str
    average_sentiment_score: float
    positive_percentage: float
    negative_percentage: float
    neutral_percentage: float
    total_reviews: int