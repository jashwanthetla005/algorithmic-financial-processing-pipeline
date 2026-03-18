from pydantic import BaseModel, field_validator
from typing import Optional


class CompanySchema(BaseModel):

    company_id: str
    parent_company_id: Optional[str] = None
    company_name: str
    assets: float
    liabilities: float
    revenue: Optional[float] = None

    @field_validator("assets", "liabilities", "revenue", mode="before")
    def clean_numbers(cls, v):

        if v is None:
            return 0

        if isinstance(v, str):
            try:
                return float(v)
            except:
                return 0

        return v