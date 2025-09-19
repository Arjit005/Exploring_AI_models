from langchain_huggingface import HuggingFaceEndpoint
from langchain_huggingface.chat_models import ChatHuggingFace
from langchain.schema import HumanMessage

# Create API-based LLM (use this after getting proper token)
llm = HuggingFaceEndpoint(
    repo_id="microsoft/DialoGPT-small",
    huggingfacehub_api_token="YOUR_NEW_TOKEN_HERE",
    temperature=0.7,
    max_new_tokens=100
)

# Create chat model
model = ChatHuggingFace(llm=llm)

# Ask question
response = model.invoke([HumanMessage(content="Who is Modi?")])
print("Response:", response.content)