import ollama
class SmartAgent:
    def __init__(self, model):
        self.model_name = model
        self.chat_log = []
        self.parts = []
        self.chat_log.append({'role':'user' , 'content':"I want your answers to be only plain text messages on a single line, separated by only one newline and no '*' signs" })
        print("Agent is created!")
    def chat(self, message):
        self.chat_log.append({'role':'user' , 'content':message })
        answer = ollama.chat( model=self.model_name , messages= self.chat_log)
        self.parts = answer['message']['content'].split(", ",-1)
        return self.parts[-1]
