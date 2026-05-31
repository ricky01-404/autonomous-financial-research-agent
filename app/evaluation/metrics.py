import time


def evaluate_agent(
    query,
    tool_results,
    synthesis,
    response,
    execution_time
):

    metrics = {}

    # -----------------------------------
    # BASIC METRICS
    # -----------------------------------

    metrics["query_length"] = len(query)

    metrics["response_length"] = len(response)

    metrics["tools_used"] = len(tool_results)

    metrics["execution_time_seconds"] = round(
        execution_time,
        2
    )

    # -----------------------------------
    # MEMORY METRICS
    # -----------------------------------

    metrics["memory_utilized"] = True

    # -----------------------------------
    # TOOL SUCCESS RATE
    # -----------------------------------

    successful_tools = 0

    for observation in tool_results:

        if "result" in observation:
            successful_tools += 1

    metrics["tool_success_rate"] = (
        successful_tools / len(tool_results)
        if tool_results else 0
    )

    # -----------------------------------
    # SYNTHESIS METRICS
    # -----------------------------------

    metrics["bullish_signals"] = len(
        synthesis.get("bullish_signals", [])
    )

    metrics["bearish_signals"] = len(
        synthesis.get("bearish_signals", [])
    )

    metrics["risk_signals"] = len(
        synthesis.get("risks", [])
    )

    metrics["opportunity_signals"] = len(
        synthesis.get("opportunities", [])
    )

    metrics["conflict_detection"] = len(
        synthesis.get("conflicts", [])
    )

    # -----------------------------------
    # QUALITY HEURISTICS
    # -----------------------------------

    metrics["has_sec_context"] = (
        "SEC" in response or
        "filing" in response.lower()
    )

    metrics["has_risk_analysis"] = (
        "risk" in response.lower()
    )

    metrics["has_growth_analysis"] = (
        "growth" in response.lower()
    )

    metrics["professional_tone"] = (
        len(response.split()) > 100
    )

    # -----------------------------------
    # OVERALL SCORE
    # -----------------------------------

    score = 0

    if metrics["tool_success_rate"] > 0.7:
        score += 20

    if metrics["has_sec_context"]:
        score += 20

    if metrics["has_risk_analysis"]:
        score += 20

    if metrics["has_growth_analysis"]:
        score += 20

    if metrics["professional_tone"]:
        score += 20

    metrics["overall_score"] = score

    return metrics