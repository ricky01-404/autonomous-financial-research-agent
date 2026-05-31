import yfinance as yf


def get_stock_data(ticker):

    stock = yf.Ticker(ticker)

    info = stock.info

    data = {
        "company": info.get("longName"),
        "sector": info.get("sector"),
        "market_cap": info.get("marketCap"),
        "current_price": info.get("currentPrice"),
        "pe_ratio": info.get("trailingPE"),
        "revenue_growth": info.get("revenueGrowth"),
        "profit_margin": info.get("profitMargins")
    }

    return data