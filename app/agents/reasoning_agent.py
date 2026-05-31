from app.tools.tool_registry import TOOLS
from app.utils.ticker_extractor import extract_ticker


def analyze_query(query):

    query_lower = query.lower()

    selected_tools = []

    # Detect ticker
    ticker = extract_ticker(query)

    # Tool selection logic

    if "news" in query_lower or "latest" in query_lower:
        selected_tools.append("company_news")

    if (
        "ratio" in query_lower
        or "metrics" in query_lower
        or "valuation" in query_lower
    ):
        selected_tools.append("financial_metrics")

    # Default tool
    selected_tools.append("stock_data")

    return {
        "ticker": ticker,
        "tools": list(set(selected_tools))
    }


def execute_tools(query):

    plan = analyze_query(query)

    ticker = plan["ticker"]

    if not ticker:
        return {"error": "Could not identify company ticker"}

    results = {}

    for tool_name in plan["tools"]:

        tool_function = TOOLS[tool_name]

        try:

            if tool_name == "company_news":
                results[tool_name] = tool_function(ticker)

            else:
                results[tool_name] = tool_function(ticker)

        except Exception as e:

            results[tool_name] = {
                "error": str(e)
            }

    return results