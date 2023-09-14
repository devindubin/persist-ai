import openai
import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv('OPEN_AI_KEY')

class Chat:

    def __init__(self):
        self.history = [{"role":"system","content":"You are an intake assistant for a law firm."}]

    def add_message(self, message, role):
        self.history.append({"role":role,"content":message})

    def get_conversation_history(self):
        return [message for message in self.history]
    
    async def get_response(self):
        conversation_history = self.get_conversation_history()
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages = conversation_history
        )
        response_set = response.choices[0].message
        self.add_message(message=response_set.get('content'),role=response_set.get('role'))
        return response_set.get('content')
    

    

