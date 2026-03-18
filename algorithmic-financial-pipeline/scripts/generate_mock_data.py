import json
import random
import uuid
from faker import Faker

fake = Faker()

def generate_company(parent_id=None):

    company_id = str(uuid.uuid4())

    record = {
        "company_id": company_id,
        "parent_company_id": parent_id,
        "company_name": fake.company(),
        "assets": random.randint(100000, 50000000),
        "liabilities": random.randint(50000, 20000000),
        "revenue": random.randint(10000, 10000000)
    }

    if random.random() < 0.15:
        record["assets"] = "unknown"

    if random.random() < 0.10:
        del record["revenue"]

    return record


def generate_dataset(num_companies=1000):

    companies = []
    parent_ids = []

    for _ in range(num_companies):

        parent = random.choice(parent_ids) if parent_ids else None
        company = generate_company(parent)

        parent_ids.append(company["company_id"])
        companies.append(company)

    return companies


def main():

    data = generate_dataset(2000)

    with open("data/raw/financial_data.json", "w") as f:
        json.dump(data, f, indent=2)


if __name__ == "__main__":
    main()