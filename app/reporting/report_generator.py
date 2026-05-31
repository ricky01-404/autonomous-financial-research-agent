def generate_report_prompt(
    query,
    tool_results,
    synthesis,
    sec_context
):

    prompt = f"""
You are a senior financial analyst.

Generate a professional investment research report.

User Query:
{query}

Tool Results:
{tool_results}

Synthesis Analysis:
{synthesis}

SEC Filing Context:
{sec_context}

The report MUST contain:

1. Executive Summary
2. Company Overview
3. Financial Analysis
4. Market Sentiment
5. SEC Filing Insights
6. Key Risks
7. Growth Opportunities
8. Final Investment Recommendation

Requirements:
- Use professional tone
- Use evidence-backed reasoning
- Mention SEC findings when relevant
- Mention risks and opportunities
- Be detailed and structured
"""

    return prompt