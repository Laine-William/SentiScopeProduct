# API RESTful d'Analyse de Sentiments de Commentaires Produits

Cette API permet d'analyser automatiquement le sentiment des commentaires utilisateurs sur des produits en utilisant la bibliothèque NLTK et son module sentiment.vader.

## Fonctionnalités

- Gestion d'un catalogue de produits (création, consultation)
- Soumission et consultation de commentaires textuels pour les produits
- Analyse automatique du sentiment de chaque commentaire
- Stockage des produits, commentaires et scores de sentiment dans une base de données
- Statistiques agrégées sur le sentiment par produit

## Technologies utilisées

- Python 3.x
- FastAPI (Framework Web API)
- NLTK (Analyse de Sentiment)
- SQLAlchemy (ORM)
- SQLite (Base de données)

## Gestion de projet

[Laine-William/sentiment-api-ntlk](https://github.com/users/Laine-William/projects/1)

## Installation

1. Cloner le dépôt :

   ```
   git clone https://github.com/votre-utilisateur/SentiScopeProduct.git
   cd SentiScopeProduct
   ```

2. Créer un environnement virtuel (recommandé) :

   ```
   python -m venv venv
   Sur linux : source venv/bin/activate
   Sur Windows : .\venv\Scripts\activate
   ```

3. Installer les dépendances :
   ```
   pip install -r requirements.txt
   ```

## Configuration de la base de données

Par défaut, l'application utilise SQLite, qui ne nécessite pas de configuration supplémentaire. La base de données sera créée automatiquement lors du premier lancement de l'application.

## Lancement de l'API

```
uvicorn app.main:app --reload
```

L'API sera accessible à l'adresse : http://127.0.0.1:8000

L'interface Swagger UI (documentation interactive) sera disponible à : http://127.0.0.1:8000/docs

## Endpoints disponibles

### Gestion des Produits

- `POST /products` : Créer un nouveau produit
- `GET /products/{product_id}` : Obtenir un produit par son ID
- `GET /products` : Obtenir la liste de tous les produits

### Gestion des Commentaires

- `POST /reviews` : Créer un nouveau commentaire avec analyse de sentiment
- `GET /reviews/product/{product_id}` : Obtenir tous les commentaires pour un produit

### Analyse de Sentiments

- `GET /products/{product_id}/sentiment_summary` : Obtenir un résumé des sentiments pour un produit

## Exemple d'utilisation

### Créer un produit

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/products/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Smartphone XYZ",
  "description": "Le dernier smartphone avec des fonctionnalités avancées"
}'
```

### Ajouter un commentaire avec analyse de sentiment

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/reviews/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "product_id": 1,
  "user_name": "Jean Dupont",
  "comment_text": "Ce produit est excellent, je suis très satisfait de mon achat !"
}'
```

### Obtenir le résumé des sentiments pour un produit

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/products/1/sentiment_summary' \
  -H 'accept: application/json'
```
