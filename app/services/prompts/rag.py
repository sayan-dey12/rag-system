from langchain_core.documents import Document

from app.services.prompts.base import BasePromptBuilder


class RAGPromptBuilder(BasePromptBuilder):

    def build(
        self,
        query: str,
        documents: list[tuple[Document, float]],
    ) -> str:

        context = "\n\n".join(
            f"""Page {document.metadata.get("page_label")}

        {document.page_content}
        """
            for document, score in documents
        )

        return f"""You are a helpful AI assistant.

Answer the user's question ONLY from the provided context.

If the context does not contain the answer, reply:

"I don't know based on the provided documents."

--------------------
Context

{context}

--------------------
Question

{query}

--------------------
Answer
"""