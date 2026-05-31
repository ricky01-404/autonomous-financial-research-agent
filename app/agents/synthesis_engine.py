def synthesize_results(tool_results):

    synthesis = {
        "bullish_signals": [],
        "bearish_signals": [],
        "risks": [],
        "opportunities": [],
        "conflicts": []
    }

    for observation in tool_results:

        tool = observation.get("tool")

        result = observation.get("result")

        # -----------------------------------
        # STOCK DATA ANALYSIS
        # -----------------------------------

        if tool == "stock_data" and isinstance(result, dict):

            pe_ratio = result.get("pe_ratio")

            revenue_growth = result.get("revenue_growth")

            if revenue_growth and revenue_growth > 0.1:

                synthesis["bullish_signals"].append(
                    "Strong revenue growth"
                )

            if pe_ratio and pe_ratio > 40:

                synthesis["risks"].append(
                    "High valuation risk"
                )

        # -----------------------------------
        # FINANCIAL METRICS
        # -----------------------------------

        if tool == "financial_metrics" and isinstance(result, dict):

            debt = result.get("debt_to_equity")

            roe = result.get("return_on_equity")

            if roe and roe > 0.15:

                synthesis["opportunities"].append(
                    "Strong return on equity"
                )

            if debt and debt > 150:

                synthesis["risks"].append(
                    "High debt levels"
                )

        # -----------------------------------
        # NEWS ANALYSIS
        # -----------------------------------

        if tool == "company_news" and isinstance(result, list):

            if len(result) > 0:

                synthesis["bullish_signals"].append(
                    "Active market/media attention"
                )

        # -----------------------------------
        # SEC FILINGS
        # -----------------------------------

        if tool == "sec_filing":

            synthesis["risks"].append(
                "SEC filings should be reviewed for regulatory risks"
            )

    # -----------------------------------
    # CONFLICT DETECTION
    # -----------------------------------

    if (
        synthesis["bullish_signals"]
        and synthesis["risks"]
    ):

        synthesis["conflicts"].append(
            "Company shows both growth opportunities and investment risks"
        )

    return synthesis