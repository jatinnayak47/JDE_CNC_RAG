from app.embeddings.embedding_service import (
    EmbeddingService
)

from app.vectorstore.qdrant_service import (
    QdrantService
)

from app.llm.llm_factory import (
    LLMFactory
)


class RAGService:

    @staticmethod
    def answer_question(
        question: str,
        top_k: int = 5
    ):

        query_embedding = (
            EmbeddingService.generate_embedding(
                question
            )
        )

        results = QdrantService.search(
            query_embedding=query_embedding,
            top_k=top_k
        )

        context_chunks = []

        for result in results:

            context_chunks.append(
                result.payload["text"]
            )

        context = "\n\n".join(
            context_chunks
        )

        prompt = f"""
You are a JD Edwards CNC assistant.

Rules:
1. Use ONLY the provided context.
2. Do not make up information.
3. If the answer is not found in the context, respond:
   "I could not find the answer in the provided documents."
4. Keep the answer concise.

Context:
{context}

Question:
{question}

Answer:
"""

        llm = (
            LLMFactory.get_llm()
        )

        answer = llm.generate(
            prompt
        )

        return {
            "question": question,
            "answer": answer,
            "sources": len(results)
        }