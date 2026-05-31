from app.tools.stock_tool import get_stock_data
from app.tools.news_tool import get_company_news
from app.tools.financial_metrics_tool import get_financial_metrics
from app.tools.sec_tool import download_sec_filing


TOOLS = {

    "stock_data": get_stock_data,

    "company_news": get_company_news,

    "financial_metrics": get_financial_metrics,
    
    "sec_filing": download_sec_filing
}