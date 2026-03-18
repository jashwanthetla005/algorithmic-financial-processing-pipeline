def calculate_leverage_ratio(financials):

    assets = financials["assets"]
    liabilities = financials["liabilities"]

    equity = assets - liabilities

    if equity <= 0:
        return float("inf")

    return liabilities / equity