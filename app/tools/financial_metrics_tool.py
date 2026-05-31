import yfinance as yf


def get_financial_metrics(ticker):

    stock = yf.Ticker(ticker)

    info = stock.info

    metrics = {
        "forward_pe": info.get("forwardPE"),
        "peg_ratio": info.get("pegRatio"),
        "beta": info.get("beta"),
        "dividend_yield": info.get("dividendYield"),
        "return_on_equity": info.get("returnOnEquity"),
        "debt_to_equity": info.get("debtToEquity")
    }

    return metrics