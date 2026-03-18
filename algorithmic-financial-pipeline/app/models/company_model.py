from sqlalchemy import Column, String, Float
from app.db.database import Base

class Company(Base):
    __tablename__ = "companies"

    company_id = Column(String(50), primary_key=True, index=True)
    name = Column(String(100))
    sector = Column(String(100))
    debt = Column(Float)
    equity = Column(Float)