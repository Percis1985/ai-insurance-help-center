from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Article
from app.schemas import ChatRequest, ChatResponse
from app.services.embedding_service import create_embedding
from app.services.ai_service import generate_ai_answer
from app.services.cache_service import get_cached_response, set_cached_response

router = APIRouter(prefix="/api/chat", tags=["AI Assistant"])


@router.post("/", response_model=ChatResponse)
def chat_with_assistant(request: ChatRequest, db: Session = Depends(get_db)):
    cached_data = get_cached_response(request.question)

    if cached_data:
        return ChatResponse(**cached_data)

    question_embedding = create_embedding(request.question)

    similar_articles = (
        db.query(Article)
        .order_by(Article.embedding.cosine_distance(question_embedding))
        .limit(2)
        .all()
    )

    if not similar_articles:
        response_data = {
            "answer": "I could not find relevant insurance help content for your question.",
            "sources": []
        }

        set_cached_response(request.question, response_data)

        return ChatResponse(**response_data)

    context = "\n\n".join(
        [
            f"Title: {article.title}\nContent: {article.content[:700]}"
            for article in similar_articles
        ]
    )

    source_titles = [article.title for article in similar_articles]

    answer = generate_ai_answer(
        question=request.question,
        context=context
    )

    response_data = {
        "answer": answer,
        "sources": source_titles
    }

    set_cached_response(request.question, response_data)

    return ChatResponse(**response_data)