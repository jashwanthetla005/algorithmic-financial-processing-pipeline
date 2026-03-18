import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.services.ingestion_service import load_and_validate_data
from app.services.graph_service import build_corporate_graph, calculate_group_financials
from app.services.risk_service import calculate_leverage_ratio


companies = load_and_validate_data("data/raw/financial_data.json")

graph = build_corporate_graph(companies)

root_company = companies[0].company_id

financials = calculate_group_financials(root_company, companies, graph)

leverage = calculate_leverage_ratio(financials)

print("Group Financials:")
print(financials)

print("\nLeverage Ratio:")
print(leverage)