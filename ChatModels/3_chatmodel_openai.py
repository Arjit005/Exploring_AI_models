import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the model
model = ChatOpenAI(model='gpt 3.5 turbo', api_key=api_key)

# Send a message
resp = model([HumanMessage(content="Hello gpt, how are you?")])

# Print response
print(resp.content)
