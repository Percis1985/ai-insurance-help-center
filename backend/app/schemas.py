from pydantic import BaseModel
from typing import Optional, List


class ArticleBase(BaseModel):
    title: str
    category: str
    content: str
    tags: Optional[str] = None


class ArticleCreate(ArticleBase):
    pass


class ArticleResponse(ArticleBase):
    id: int

    class Config:
        from_attributes = True


class ChatRequest(BaseModel):
    question: str


class ChatResponse(BaseModel):
    answer: str
    sources: List[str] = []