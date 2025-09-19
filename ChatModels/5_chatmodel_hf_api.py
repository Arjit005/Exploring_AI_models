from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
import os
from dotenv import load_dotenv

load_dotenv()
api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",  # Supported chat model
    huggingfacehub_api_token=api_token,
)

chat_model = ChatHuggingFace(llm=llm)
response = chat_model.invoke("What is capital of India?")
print(response.content)
