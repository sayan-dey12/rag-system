from langchain_core.documents import Document

from app.services.prompts.base import BasePromptBuilder


class RAGPromptBuilder(BasePromptBuilder):

    def build(
        self,
        query: str,
        documents: list[tuple[Document, float]],
    ) -> str:

        context = "\n\n".join(
            f"""
        Document: {doc.metadata['source']}
        Page: {doc.metadata['page_label']}

        {doc.page_content}
        """
            for doc, _ in documents
        )

        return f"""You are a helpful AI assistant.

Answer the user's question ONLY using the provided context.

Guidelines:

1. If the answer exists in the context, answer naturally and clearly.
2. Do not make up information.
3. If the answer cannot be found in the context, respond exactly with:
   "I don't know based on the provided documents."
4. When your answer uses information from one or more context sections,
   end your response with a section titled:

   Sources

   For every page you used, list:

   - Page <page number>
   - File: <file name>

5. Only cite pages that actually contributed to the answer.
6. Never invent page numbers or file names.

--------------------
Context

{context}

--------------------
Question

{query}

--------------------
Answer
"""