from app.services.rag.factory import RAGFactory
from app.events.printer import print_event
from app.services.rag.factory import RAGFactory

rag = RAGFactory.get_service()

def event(message: str):
    print(message)


# generate all in one go
# answer = rag.ask(
#     "Explain Breadth First Search. give a very long answer",
#      on_event=print_event,
# )

# print(answer)



# stream the answer
for token in rag.stream(
    "What is Big O?",
    on_event=print_event,
):
    print(token, end="", flush=True)