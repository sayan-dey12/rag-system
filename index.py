from app.services.retrieval.factory import RetrieverFactory


retriever = RetrieverFactory.get_retriever()

documents = retriever.retrieve(
    "What is Breadth First Search?"
)

results = retriever.retrieve("Breadth First Search")

print("=" * 60)

for index, (document, score) in enumerate(results, start=1):

    print("=" * 60)
    print(f"Result : {index}")
    print(f"Score  : {score:.4f}")
    print(f"Page   : {document.metadata.get('page_label')}")
    print(document.page_content[:300])


# from app.services.retrieval.factory import RetrieverFactory

# print("Starting...")

# retriever = RetrieverFactory.get_retriever()

# documents = retriever.retrieve(
#     "Breadth First Search"
# )

# print(f"Documents: {len(documents)}")

# for doc in documents:
#     print(doc.page_content)