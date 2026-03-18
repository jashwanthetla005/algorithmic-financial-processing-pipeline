import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.services.ingestion_service import load_and_validate_data
from app.services.graph_service import build_corporate_graph, calculate_group_financials


companies = load_and_validate_data("data/raw/financial_data.json")

graph = build_corporate_graph(companies)

root_company = companies[0].company_id

result = calculate_group_financials(root_company, companies, graph)

print("Group Financials:")
print(result)