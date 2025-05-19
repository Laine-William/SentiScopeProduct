from fastapi import FastAPI

from app.models.database import Base, engine
from app.routers import products, reviews

# Créer les tables dans la base de données
Base.metadata.create_all(bind=engine)

# Initialiser l'application FastAPI
app = FastAPI(
    title="Product Sentiment Analysis API",
    description="API RESTful pour l'analyse de sentiments des commentaires de produits",
    version="1.0.0",
)

# Inclure les routeurs
app.include_router(products.router)
app.include_router(reviews.router)

@app.get("/")
def read_root():
    return {
        "message": "Bienvenue sur l'API d'analyse de sentiments des commentaires de produits",
        "documentation": "/docs"
    }