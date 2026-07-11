class ChatService:

    _history = []

    @classmethod
    def add_message(
        cls,
        question: str,
        answer: str
    ):

        cls._history.append(
            {
                "question": question,
                "answer": answer
            }
        )

        # Keep only last 5 conversations
        cls._history = cls._history[-10:]

    @classmethod
    def get_context(
        cls
    ):

        history = []

        for item in cls._history:

            history.append(
                f"User: {item['question']}"
            )

            history.append(
                f"Assistant: {item['answer']}"
            )

        return "\n".join(history)

    @classmethod
    def clear(
        cls
    ):

        cls._history = []