from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from openai import OpenAI
import os

# ========================
# INIT
# ========================
app = FastAPI()

# ✅ CORS (VERY IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ========================
# DB
# ========================
DATABASE_URL = "sqlite:///./events.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class EventDB(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    date = Column(String)
    description = Column(String)

Base.metadata.create_all(bind=engine)

# ========================
# MODELS
# ========================
class Event(BaseModel):
    name: str
    date: str
    description: str

class ChatRequest(BaseModel):
    message: str

# ========================
# DB DEPENDENCY
# ========================
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ========================
# AI FUNCTION
# ========================
def ai_response(prompt: str):
    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an AI event planner."},
            {"role": "user", "content": prompt}
        ]
    )
    return res.choices[0].message.content

# ========================
# ROUTES
# ========================
@app.get("/events")
def get_events(db: Session = Depends(get_db)):
    return db.query(EventDB).all()

@app.post("/events")
def create_event(event: Event, db: Session = Depends(get_db)):
    existing = db.query(EventDB).filter(EventDB.date == event.date).first()
    if existing:
        raise HTTPException(status_code=400, detail="Conflict detected")

    new_event = EventDB(**event.dict())
    db.add(new_event)
    db.commit()
    db.refresh(new_event)

    return new_event

@app.post("/ai/chat")
def chat(req: ChatRequest):
    return {"reply": ai_response(req.message)}