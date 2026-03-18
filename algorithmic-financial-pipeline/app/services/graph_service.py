from collections import defaultdict


def build_corporate_graph(companies):

    graph = defaultdict(list)

    for company in companies:

        parent = company.parent_company_id

        if parent:
            graph[parent].append(company.company_id)

    return graph

def calculate_group_financials(root_id, companies, graph):

    company_map = {c.company_id: c for c in companies}

    visited = set()

    total_assets = 0
    total_liabilities = 0
    total_revenue = 0


    def dfs(company_id):

        nonlocal total_assets, total_liabilities, total_revenue

        if company_id in visited:
            return

        visited.add(company_id)

        company = company_map.get(company_id)

        if company:
            total_assets += company.assets or 0
            total_liabilities += company.liabilities or 0
            total_revenue += company.revenue or 0

        for child in graph.get(company_id, []):
            dfs(child)


    dfs(root_id)

    return {
        "assets": total_assets,
        "liabilities": total_liabilities,
        "revenue": total_revenue
    }