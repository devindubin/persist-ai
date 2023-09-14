import os
from dotenv import load_dotenv
load_dotenv()
import openai

# Set OpenAI key
openai.api_key = os.getenv('OPEN_AI_KEY')
print(os.getenv('OPEN_AI_KEY'))
# Connect to OpenAI client
client = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a call center agent working for a law firm."},
        {"role":"user","content":"Hello, I need help."}
    ]
)

print(client.choices)

def initialize_conversation():
  messages = [{
        "role":"system",
        "content": "You are a call center agent working for a law firm. Your tone should be sympathetic and you should focus on collecting as much contact information as possible."
    }]

  chat = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = messages
  )
  return chat

def append_response(message)