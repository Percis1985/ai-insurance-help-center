AI Insurance Help Center

A modern AI-powered customer support portal for a fictional insurance company.

Repository:
https://github.com/Percis1985/ai-insurance-help-center

Built using:

Frontend: React (Vite) + Tailwind CSS
Backend: FastAPI (Python)
Database: PostgreSQL + pgvector
AI: Google Gemini

The application allows users to:

Browse insurance help topics
Search for answers
Ask questions to an AI assistant
Receive contextual, step-by-step guidance

Setup Instructions
1. Clone the repository
gitclone https://github.com/Percis1985/ai-insurance-help-center.git
cd ai-insurance-help-center
2. Start Database (PostgreSQL + pgvector)

Make sure Docker Desktop is running.

docker compose up -d

Verify:

docker ps
3. Backend Setup (FastAPI)
cd backend
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt

Seed initial data:

python -m app.seed_data

Run backend:

uvicorn app.main:app --reload

Open API docs:

http://localhost:8000/docs
4. Frontend Setup (React)

Open a new terminal:

cd frontend
npm install
npm run dev

Open UI:

http://localhost:5173
Environment Configuration

Create file:

backend/.env

Add:

DATABASE_URL=postgresql://postgres:postgres@localhost:5432/insurance_help_center

GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL=gemini-2.5-flash-lite
🤖 AI Provider Used
Provider: Google Gemini
Model: gemini-2.5-flash-lite
Used to generate structured insurance guidance based on retrieved content
🧠 Architecture Overview
React Frontend (Vite)
        ↓
FastAPI Backend
        ↓
PostgreSQL + pgvector (Vector Search)
        ↓
Gemini AI (Response Generation)
Flow:
User enters a question
Backend generates embedding
pgvector retrieves similar articles
Relevant context sent to Gemini (RAG)
AI generates structured answer
Response displayed in UI
⚡ Performance Optimizations
In-memory caching for repeated queries
Embedding caching to reduce recomputation
Reduced prompt size for faster AI response
Fast Gemini model (flash-lite)
⚖️ Tradeoffs and Assumptions
Tradeoffs:
Used in-memory caching instead of Redis (simpler setup)
Limited dataset (demo-level insurance content)
Synchronous AI calls (simpler implementation)
Assumptions:
Users ask general insurance queries
Help center data is static
AI responses are advisory only
🧪 Testing
Backend Tests
cd backend
python -m pytest
Frontend Tests
cd frontend
npm test
📌 Features
Help center browsing
Search functionality
AI assistant with RAG
Clean UI (Tailwind CSS)
Unit testing (frontend + backend)