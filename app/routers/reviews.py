from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.models.database import get_db
from app.models.product import Product
from app.models.review import Review
from app.schemas.schemas import Review as ReviewSchema, ReviewCreate
from app.services.sentiment import analyze_sentiment

router = APIRouter(
    prefix="/reviews",
    tags=["reviews"],
)

@router.post("/", response_model=ReviewSchema, status_code=201)
def create_review(review: ReviewCreate, db: Session = Depends(get_db)):
    # Vérifier que le produit existe
    product = db.query(Product).filter(Product.id == review.product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    # Analyser le sentiment du commentaire
    sentiment_scores = analyze_sentiment(review.comment_text)
    compound_score = sentiment_scores['compound']
    
    # Créer le commentaire avec le score de sentiment
    db_review = Review(
        product_id=review.product_id,
        user_name=review.user_name,
        comment_text=review.comment_text,
        sentiment_compound_score=compound_score
    )
    
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    
    return db_review

@router.get("/product/{product_id}", response_model=List[ReviewSchema])
def get_product_reviews(product_id: int, db: Session = Depends(get_db)):
    # Vérifier que le produit existe
    product = db.query(Product).filter(Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    # Récupérer tous les commentaires pour ce produit
    reviews = db.query(Review).filter(Review.product_id == product_id).all()
    
    return reviews