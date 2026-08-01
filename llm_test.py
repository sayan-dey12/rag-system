from app.services.llm.factory import LLMFactory


llm = LLMFactory.get_llm()

answer = llm.generate(
    "Explain Breadth First Search in two sentences."
)

print(answer)