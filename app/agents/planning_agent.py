from groq import Groq
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

AVAILABLE_TOOLS = [
    "stock_data",
    "company_news",
    "financial_metrics",
    "sec_filing"
]


def create_research_plan(query):

    prompt = f"""
You are an autonomous financial research planner.

Available Tools:
{AVAILABLE_TOOLS}

User Query:
{query}

Your task:
Create a research plan using ONLY the available tools.

STRICT RULES:
- Return ONLY valid JSON
- Do NOT add explanations
- Do NOT use markdown
- Do NOT wrap in ```json
- Output must be parseable with json.loads()

Required Format:

{{
    "steps": [
        {{
            "tool": "stock_data",
            "reason": "Analyze company fundamentals"
        }},
        {{
            "tool": "company_news",
            "reason": "Analyze market sentiment"
        }}
    ]
}}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    content = response.choices[0].message.content

    print("\nRAW PLANNER OUTPUT:\n")
    print(content)

    try:

        # Clean accidental markdown
        content = content.replace("```json", "")
        content = content.replace("```", "")

        parsed = json.loads(content)

        return parsed

    except Exception as e:

        print("\nPLANNER ERROR:")
        print(e)

        return {
            "steps": [
                {
                    "tool": "stock_data",
                    "reason": "Fallback default research"
                }
            ]
        }