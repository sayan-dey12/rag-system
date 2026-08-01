from app.services.rag.factory import RAGFactory

rag = RAGFactory.get_service()

# generate all in one go
# answer = rag.ask(
#     "Explain Breadth First Search. give a very long answer"
# )

# print(answer)



# stream the answer
for token in rag.stream(
    "Explain Breadth First Search. give a very long answer"
):
    print(token, end="", flush=True)