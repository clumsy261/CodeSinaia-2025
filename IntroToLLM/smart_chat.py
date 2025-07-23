import ollama
from smart_agent import SmartAgent

chat_log = []
smart_agent = SmartAgent("gemma3")

question = input("Pregunta? >")
question = question.strip()
while question != "/adios":
    if question != "":
        answer = smart_agent.chat(question)
        print(answer)
    question = input("Uno mas pregunta? >")
    question = question.strip()
