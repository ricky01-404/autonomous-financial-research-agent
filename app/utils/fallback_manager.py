import time

from app.memory.vector_memory import VectorMemory

vector_memory = VectorMemory()


MAX_RETRIES = 2


def execute_with_fallback(
    tool_function,
    tool_name,
    ticker
):

    # -----------------------------------
    # RETRY LOOP
    # -----------------------------------

    for attempt in range(MAX_RETRIES):

        try:

            result = tool_function(ticker)

            return {
                "status": "success",
                "source": "live_tool",
                "result": result
            }

        except Exception as e:

            print(
                f"{tool_name} failed "
                f"(Attempt {attempt + 1})"
            )

            time.sleep(1)

    # -----------------------------------
    # VECTOR MEMORY FALLBACK
    # -----------------------------------

    try:

        fallback_results = vector_memory.search_memory(
            f"{ticker} financial analysis"
        )

        return {
            "status": "fallback",
            "source": "vector_memory",
            "result": fallback_results
        }

    except Exception as e:

        return {
            "status": "failed",
            "source": "none",
            "error": str(e)
        }