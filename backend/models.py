from sqlalchemy import Column, Integer, String
from database import Base

class EventDB(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    date = Column(String)
    description = Column(String)