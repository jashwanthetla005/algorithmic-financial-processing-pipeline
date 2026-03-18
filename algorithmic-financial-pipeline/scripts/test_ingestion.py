import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.services.ingestion_service import load_and_validate_data

data = load_and_validate_data("data/raw/financial_data.json")

print("Total clean records:", len(data))
print(data[0])