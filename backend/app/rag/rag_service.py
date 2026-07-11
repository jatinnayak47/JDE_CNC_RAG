from app.embeddings.embedding_service import (
    EmbeddingService
)

from app.vectorstore.qdrant_service import (
    QdrantService
)

from app.llm.llm_factory import (
    LLMFactory
)

from app.chat.chat_service import (
    ChatService
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

        conversation_context = (
            ChatService.get_context()
        )

        prompt = f"""
You are an expert JD Edwards CNC consultant.

Instructions:
1. Use ONLY the provided context.
2. Use conversation history when resolving references.
3. Do not make up information.
4. If the answer is not found in the context, respond:
   "I could not find the answer in the provided documents."
5. Focus on JD Edwards EnterpriseOne and CNC concepts.
6. Keep the answer concise but complete.

Conversation History:
{conversation_context}

Retrieved Context:
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

        ChatService.add_message(
            question=question,
            answer=answer
        )

        source_details = []

        for result in results:

            source_details.append(
                {
                    "document_id":
                        result.payload.get(
                            "document_id"
                        ),
                    "chunk_index":
                        result.payload.get(
                            "chunk_index"
                        ),
                    "score":
                        result.score
                }
            )

        return {
            "question": question,
            "answer": answer,
            "source_count": len(results),
            "sources": source_details
        }