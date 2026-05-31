import chromadb
import uuid


class VectorMemory:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="data/chroma_db"
        )

        self.collection = self.client.get_or_create_collection(
            name="financial_memory"
        )

    def store_memory(self, text):

        self.collection.add(
            documents=[text],
            ids=[str(uuid.uuid4())]
        )

    def search_memory(self, query, n_results=3):

        results = self.collection.query(
            query_texts=[query],
            n_results=n_results
        )

        return results