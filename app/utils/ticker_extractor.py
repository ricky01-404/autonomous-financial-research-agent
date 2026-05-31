COMPANY_TICKERS = {

    # Technology
    "apple": "AAPL",
    "microsoft": "MSFT",
    "google": "GOOGL",
    "alphabet": "GOOGL",
    "amazon": "AMZN",
    "meta": "META",
    "facebook": "META",
    "nvidia": "NVDA",
    "intel": "INTC",
    "amd": "AMD",
    "oracle": "ORCL",
    "salesforce": "CRM",
    "adobe": "ADBE",
    "netflix": "NFLX",
    "paypal": "PYPL",
    "uber": "UBER",
    "airbnb": "ABNB",
    "spotify": "SPOT",
    "shopify": "SHOP",
    "snap": "SNAP",

    # EV / Automotive
    "tesla": "TSLA",
    "ford": "F",
    "general motors": "GM",
    "toyota": "TM",
    "rivian": "RIVN",

    # Finance
    "jpmorgan": "JPM",
    "goldman sachs": "GS",
    "bank of america": "BAC",
    "wells fargo": "WFC",
    "visa": "V",
    "mastercard": "MA",
    "american express": "AXP",
    "blackrock": "BLK",

    # Healthcare
    "pfizer": "PFE",
    "moderna": "MRNA",
    "johnson & johnson": "JNJ",
    "unitedhealth": "UNH",

    # Consumer
    "coca cola": "KO",
    "pepsi": "PEP",
    "mcdonalds": "MCD",
    "starbucks": "SBUX",
    "nike": "NKE",
    "walmart": "WMT",
    "costco": "COST",

    # Energy
    "exxon": "XOM",
    "chevron": "CVX",
    "shell": "SHEL",

    # Telecom
    "verizon": "VZ",
    "at&t": "T",
    "t mobile": "TMUS",

    # Entertainment
    "disney": "DIS",
    "warner bros": "WBD",

    # Semiconductor / AI
    "broadcom": "AVGO",
    "qualcomm": "QCOM",
    "tsmc": "TSM"
}


def extract_ticker(query):

    query = query.lower()

    for company, ticker in COMPANY_TICKERS.items():

        if company in query:
            return ticker

    return None