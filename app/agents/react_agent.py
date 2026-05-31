from app.tools.tool_registry import TOOLS
from app.utils.ticker_extractor import extract_ticker
from app.agents.planning_agent import create_research_plan
from app.utils.fallback_manager import execute_with_fallback


MAX_STEPS = 5


def react_agent(query):

    ticker = extract_ticker(query)

    if not ticker:

        return {
            "error": "Could not identify ticker."
        }

    # -----------------------------------
    # CREATE AI RESEARCH PLAN
    # -----------------------------------

    research_plan = create_research_plan(query)

    print("\nRESEARCH PLAN:")
    print(research_plan)

    observations = []

    steps = research_plan.get("steps", [])

    for step_number, step in enumerate(steps):

        tool_name = step.get("tool")

        if tool_name not in TOOLS:
            continue

        print(f"\nSTEP {step_number + 1}")
        print(f"Using Tool: {tool_name}")
        print(f"Reason: {step.get('reason')}")

        tool_function = TOOLS[tool_name]

        try:

            execution_result = execute_with_fallback(
                tool_function,
                tool_name,
                ticker
                    )

            observations.append({
                "step": step_number + 1,
                "tool": tool_name,
                "reason": step.get("reason"),
                "result": execution_result
                    })

        except Exception as e:

            observations.append({
                "step": step_number + 1,
                "tool": tool_name,
                "error": str(e)
            })

    return observations