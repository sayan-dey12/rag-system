from langchain_core.documents import Document

from app.services.prompts.base import BasePromptBuilder


class RAGPromptBuilder(BasePromptBuilder):

    def build(
        self,
        query: str,
        documents: list[tuple[Document, float]],
    ) -> str:

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

Answer the user's question ONLY using the provided context.

Guidelines:

1. If the answer exists in the context, answer naturally and clearly.
2. Never invent information.
3. If the answer is not present, reply exactly:

"I don't know based on the provided documents."

4. At the end of every answer, include a section titled:

Sources

For every source actually used, list:

- File: <file name>
- Page: <page number>

5. Never cite pages or files that were not used.

--------------------
Context

{context}

--------------------
Question

{query}

--------------------
Answer
"""