from app.tools.sec_parser import read_sec_filing
from app.utils.text_chunker import chunk_text
from app.memory.vector_memory import VectorMemory


vector_memory = VectorMemory()


def ingest_sec_filing():

    text = read_sec_filing()

    chunks = chunk_text(text)

    for chunk in chunks:

        vector_memory.store_memory(chunk)

    return f"Ingested {len(chunks)} SEC filing chunks."


def retrieve_sec_context(query):

    results = vector_memory.search_memory(query)

    return results