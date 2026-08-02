from langchain_core.documents import Document

from app.services.chat.conversation import Message
from app.services.prompts.base import BasePromptBuilder

from app.services.prompts.system import RAG_SYSTEM_PROMPT

class RAGPromptBuilder(BasePromptBuilder):

    def build(
        self,
        query: str,
        history: list[Message],
        documents: list[tuple[Document, float]],
    ) -> str:

        #
        # Conversation
        #
        conversation = "\n".join(
            f"{message.role.title()}: {message.content}"
            for message in history
        )

        #
        # Retrieved context
        #
        context_parts: list[str] = []

        for doc, _ in documents:

            metadata = doc.metadata

            file_name = (
                metadata.get("file_name")
                or metadata.get("source")
                or "Unknown Document"
            )

            page = metadata.get(
                "page_label",
                metadata.get("page", "?"),
            )

            context_parts.append(
                f"""
Document: {file_name}
Page: {page}

{doc.page_content}
"""
            )

        context = "\n\n".join(context_parts)

        return f"""
{RAG_SYSTEM_PROMPT}


--------------------
Conversation History

{conversation or "No previous conversation."}

--------------------
Retrieved Context

{context}

--------------------
Current Question

{query}

--------------------
Answer
"""