from langchain_core.documents import Document

from app.services.chat.conversation import Message
from app.services.prompts.base import BasePromptBuilder


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

        return f"""You are a helpful AI assistant.

You are having a continuous conversation with the user.

Use the conversation history when it is relevant.

Answer the CURRENT question using the retrieved context.

If the current question depends on previous messages,
use the conversation history to understand it.

Never invent facts that are not present in the retrieved context.

If the answer cannot be found in the retrieved context, reply exactly:

"I don't know based on the provided documents."

At the end of every answer include

Sources

For every source actually used, list

- File: <file name>
- Page: <page number>

Never cite documents that were not used.

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