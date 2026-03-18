import json
from app.schemas.company_schema import CompanySchema


def load_and_validate_data(file_path):

    clean_companies = []

    with open(file_path, "r") as f:
        data = json.load(f)

    for record in data:

        try:
            company = CompanySchema(**record)
            clean_companies.append(company)

        except Exception:
            continue

    return clean_companies