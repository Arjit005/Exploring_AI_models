import os
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")

model = ChatAnthropic(model="claude-3-sonnet-20240229", api_key=api_key)

resp = model.invoke("Hello Claude, how are you?")
print(resp.content)
