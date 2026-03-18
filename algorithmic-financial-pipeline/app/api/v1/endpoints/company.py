from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.company_model import Company

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/companies/{company_id}/leverage")
def get_company_leverage(company_id: str, db: Session = Depends(get_db)):

    company = db.query(Company).filter(Company.company_id == company_id).first()

    if company is None:
        raise HTTPException(status_code=404, detail="Company not found")

    if company.equity == 0:
        raise HTTPException(status_code=400, detail="Equity cannot be zero")

    leverage = company.debt / company.equity

    return {
        "company_id": company.company_id,
        "leverage": leverage
    }
@router.post("/companies")
def create_company(
    company_id: str,
    name: str,
    sector: str,
    debt: float,
    equity: float,
    db: Session = Depends(get_db)
):

    new_company = Company(
        company_id=company_id,
        name=name,
        sector=sector,
        debt=debt,
        equity=equity
    )

    db.add(new_company)
    db.commit()
    db.refresh(new_company)

    return {
        "message": "Company created successfully",
        "company": new_company.company_id
    }