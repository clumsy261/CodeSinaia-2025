import ollama
from smart_agent import SmartAgent

chat_log = []
smart_agent = SmartAgent()

question = input("Pregunta? >")
question = question.strip()
while question != "/adios":
    if question != "":
        chat_log.append({'role':'user' , 'context':question })
        answer = ollama.chat(model="gemma3" , messages=chat_log)
        answer_text = answer['message']['content']
        print(answer_text)
    question = input("Uno mas pregunta? >")
    question = question.strip()
