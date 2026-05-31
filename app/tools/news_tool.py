import requests
import os

from dotenv import load_dotenv

load_dotenv()


def get_company_news(company):

    url = f"https://newsapi.org/v2/everything?q={company}&apiKey={os.getenv('NEWS_API_KEY')}"

    try:

        response = requests.get(url)

        data = response.json()

        articles = []

        for article in data.get("articles", [])[:5]:

            articles.append({
                "title": article.get("title"),
                "source": article.get("source", {}).get("name")
            })

        return articles

    except Exception as e:

        return {"error": str(e)}