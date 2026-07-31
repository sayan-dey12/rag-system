# from app.services.retrieval.factory import RetrieverFactory


# retriever = RetrieverFactory.get_retriever()

# documents = retriever.retrieve(
#     "What is Breadth First Search?"
# )

# print("=" * 60)

# for i, doc in enumerate(documents, start=1):

#     print(f"Result {i}")
#     print(doc.page_content)
#     print(doc.metadata)
#     print("-" * 60)



from app.services.retrieval.factory import RetrieverFactory

print("Starting...")

retriever = RetrieverFactory.get_retriever()

documents = retriever.retrieve(
    "Breadth First Search"
)

print(f"Documents: {len(documents)}")

for doc in documents:
    print(doc.page_content)