from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine, Base
from app.routes import articles, search, chat

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Insurance Help Center API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(articles.router)
app.include_router(search.router)
app.include_router(chat.router)


@app.get("/")
def health_check():
    return {"message": "AI Insurance Help Center API is running"}