from app.database import SessionLocal, engine, Base
from app.models import Article
from app.services.embedding_service import create_embedding

Base.metadata.create_all(bind=engine)

db = SessionLocal()

sample_articles = [
    {
        "title": "How to Submit a Car Accident Claim",
        "category": "Claims",
        "content": "To submit a car accident claim, report the accident, take photos, collect the police report if required, complete the claim form, and upload supporting documents such as repair estimates and insurance details.",
        "tags": "car, accident, claim, motor insurance"
    },
    {
        "title": "What Does Deductible Mean?",
        "category": "Policy",
        "content": "A deductible is the amount you need to pay first before the insurance company pays the remaining approved claim amount. For example, if your deductible is $500 and the claim is $2,000, you pay $500 and the insurer pays $1,500.",
        "tags": "deductible, policy, premium, claim"
    },
    {
        "title": "Lost Luggage Travel Insurance Claim",
        "category": "Travel",
        "content": "If your luggage is lost during travel, report it to the airline immediately, get a written report, keep receipts for essential purchases, and submit the claim with travel documents and baggage report.",
        "tags": "travel, luggage, lost baggage, claim"
    },
    {
        "title": "Claim Processing Time",
        "category": "Claims",
        "content": "Claim processing time depends on the claim type and document completeness. Simple claims may take a few working days, while complex claims may take longer if additional review is required.",
        "tags": "claim, processing time, status"
    },
    {
        "title": "Term Life vs Whole Life Insurance",
        "category": "Life Insurance",
        "content": "Term life insurance provides coverage for a fixed period, such as 10, 20, or 30 years. Whole life insurance provides lifetime coverage and may include a cash value component.",
        "tags": "life insurance, term life, whole life"
    }
]

existing_count = db.query(Article).count()

if existing_count == 0:
    for item in sample_articles:
        text_for_embedding = f"{item['title']} {item['category']} {item['content']} {item['tags']}"

        article = Article(
            title=item["title"],
            category=item["category"],
            content=item["content"],
            tags=item["tags"],
            embedding=create_embedding(text_for_embedding)
        )

        db.add(article)

    db.commit()
    print("Sample articles with embeddings inserted.")
else:
    print("Articles already exist.")

db.close()