from app.services.prompts.factory import PromptFactory
from app.services.retrieval.factory import RetrieverFactory


retriever = RetrieverFactory.get_retriever()

docs = retriever.retrieve(
    "Breadth First Search"
)

builder = PromptFactory.get_builder()

prompt = builder.build(
    query="What is Breadth First Search?",
    documents=docs,
)

print(prompt)