from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import or_
from typing import List

from app.database import get_db
from app.models import Article
from app.schemas import ArticleResponse

router = APIRouter(prefix="/api/search", tags=["Search"])


@router.get("/", response_model=List[ArticleResponse])
def search_articles(q: str = Query(...), db: Session = Depends(get_db)):
    search_text = f"%{q.lower()}%"

    results = db.query(Article).filter(
        or_(
            Article.title.ilike(search_text),
            Article.content.ilike(search_text),
            Article.tags.ilike(search_text),
            Article.category.ilike(search_text),
        )
    ).all()

    return results