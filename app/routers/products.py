from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.models.database import get_db
from app.models.product import Product
from app.models.review import Review
from app.schemas import Product as ProductSchema, ProductCreate, SentimentSummary

router = APIRouter(
    prefix="/products",
    tags=["products"],
)

@router.post("/", response_model=ProductSchema, status_code=201)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = Product(name=product.name, description=product.description)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@router.get("/{product_id}", response_model=ProductSchema)
def get_product(product_id: int, db: Session = Depends(get_db)):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@router.get("/", response_model=List[ProductSchema])
def get_products(db: Session = Depends(get_db)):
    products = db.query(Product).all()
    return products

@router.get("/{product_id}/sentiment_summary", response_model=SentimentSummary)
def get_sentiment_summary(product_id: int, db: Session = Depends(get_db)):
    # Vérifier que le produit existe
    product = db.query(Product).filter(Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    # Récupérer tous les commentaires pour ce produit
    reviews = db.query(Review).filter(Review.product_id == product_id).all()
    total_reviews = len(reviews)
    
    if total_reviews == 0:
        return SentimentSummary(
            product_id=product_id,
            product_name=product.name,
            average_sentiment_score=0.0,
            positive_percentage=0.0,
            negative_percentage=0.0,
            neutral_percentage=0.0,
            total_reviews=0
        )
    
    # Calculer les statistiques de sentiment
    compound_scores = [review.sentiment_compound_score for review in reviews]
    avg_score = sum(compound_scores) / total_reviews
    
    # Compter les commentaires positifs, négatifs et neutres
    positive_reviews = sum(1 for score in compound_scores if score >= 0.05)
    negative_reviews = sum(1 for score in compound_scores if score <= -0.05)
    neutral_reviews = total_reviews - positive_reviews - negative_reviews
    
    # Calculer les pourcentages
    positive_percentage = (positive_reviews / total_reviews) * 100 if total_reviews > 0 else 0
    negative_percentage = (negative_reviews / total_reviews) * 100 if total_reviews > 0 else 0
    neutral_percentage = (neutral_reviews / total_reviews) * 100 if total_reviews > 0 else 0
    
    return SentimentSummary(
        product_id=product_id,
        product_name=product.name,
        average_sentiment_score=avg_score,
        positive_percentage=positive_percentage,
        negative_percentage=negative_percentage,
        neutral_percentage=neutral_percentage,
        total_reviews=total_reviews
    )