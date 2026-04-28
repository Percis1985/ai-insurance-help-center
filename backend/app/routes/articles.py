from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models import Article
from app.schemas import ArticleResponse

router = APIRouter(prefix="/api/articles", tags=["Articles"])


@router.get("/", response_model=List[ArticleResponse])
def get_articles(db: Session = Depends(get_db)):
    return db.query(Article).all()


@router.get("/{article_id}", response_model=ArticleResponse)
def get_article(article_id: int, db: Session = Depends(get_db)):
    article = db.query(Article).filter(Article.id == article_id).first()

    if not article:
        raise HTTPException(status_code=404, detail="Article not found")

    return article


@router.get("/category/{category_name}", response_model=List[ArticleResponse])
def get_articles_by_category(category_name: str, db: Session = Depends(get_db)):
    return db.query(Article).filter(Article.category == category_name).all()