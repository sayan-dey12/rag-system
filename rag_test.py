from app.services.rag.factory import RAGFactory

rag = RAGFactory.get_service()

answer = rag.ask(
    "What is Breadth First Search?"
)

print(answer)