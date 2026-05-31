import os
import time

from groq import Groq
from dotenv import load_dotenv

from app.agents.react_agent import react_agent
from app.agents.synthesis_engine import synthesize_results

from app.memory.short_term_memory import ShortTermMemory
from app.memory.episodic_memory import EpisodicMemory
from app.memory.vector_memory import VectorMemory

from app.rag.sec_rag import retrieve_sec_context

from app.evaluation.metrics import evaluate_agent

from app.reporting.report_generator import generate_report_prompt

from app.utils.logger import log_event, log_error

load_dotenv()

# -----------------------------------
# INITIALIZE GROQ CLIENT
# -----------------------------------

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# -----------------------------------
# INITIALIZE MEMORY SYSTEMS
# -----------------------------------

short_memory = ShortTermMemory()

episodic_memory = EpisodicMemory()

vector_memory = VectorMemory()


def financial_agent(query):

    try:

        # -----------------------------------
        # START TIMER
        # -----------------------------------

        start_time = time.time()

        log_event(f"New Query: {query}")

        # -----------------------------------
        # REACT AGENT EXECUTION
        # -----------------------------------

        tool_results = react_agent(query)

        # Handle agent errors
        if isinstance(tool_results, dict) and "error" in tool_results:

            log_error(tool_results["error"])

            return tool_results["error"]

        log_event(f"Tool Results: {tool_results}")

        # -----------------------------------
        # MULTI-SOURCE SYNTHESIS
        # -----------------------------------

        synthesis = synthesize_results(tool_results)

        log_event(f"Synthesis: {synthesis}")

        # -----------------------------------
        # SHORT-TERM MEMORY
        # -----------------------------------

        short_memory.add({
            "query": query,
            "results": tool_results
        })

        # -----------------------------------
        # EPISODIC MEMORY
        # -----------------------------------

        episodic_memory.save_episode({
            "query": query,
            "tools_used": [
                observation["tool"]
                for observation in tool_results
            ]
        })

        # -----------------------------------
        # VECTOR MEMORY STORAGE
        # -----------------------------------

        vector_memory.store_memory(
            str(tool_results)
        )

        # -----------------------------------
        # VECTOR MEMORY RETRIEVAL
        # -----------------------------------

        past_memories = vector_memory.search_memory(query)

        # -----------------------------------
        # SEC RAG RETRIEVAL
        # -----------------------------------

        sec_context = retrieve_sec_context(query)

        # -----------------------------------
        # GENERATE PROFESSIONAL REPORT PROMPT
        # -----------------------------------

        system_prompt = generate_report_prompt(
            query=query,
            tool_results=tool_results,
            synthesis=synthesis,
            sec_context=sec_context
        )

        # -----------------------------------
        # LLM RESPONSE
        # -----------------------------------

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": query
                }
            ],
            temperature=0.3
        )

        # -----------------------------------
        # FINAL RESPONSE
        # -----------------------------------

        final_response = response.choices[0].message.content

        # -----------------------------------
        # EXECUTION TIME
        # -----------------------------------

        execution_time = time.time() - start_time

        # -----------------------------------
        # EVALUATION
        # -----------------------------------

        evaluation = evaluate_agent(
            query=query,
            tool_results=tool_results,
            synthesis=synthesis,
            response=final_response,
            execution_time=execution_time
        )

        log_event(f"Evaluation Metrics: {evaluation}")

        print("\nEVALUATION METRICS:\n")
        print(evaluation)

        return final_response

    except Exception as e:

        log_error(str(e))

        return f"Agent Error: {str(e)}"


# -----------------------------------
# MAIN LOOP
# -----------------------------------

if __name__ == "__main__":

    while True:

        user_query = input(
            "\nEnter research query (or type 'exit'): "
        )

        if user_query.lower() == "exit":
            break

        result = financial_agent(user_query)

        print("\nAGENT RESPONSE:\n")

        print(result)