from langchain_huggingface.chat_models import ChatHuggingFace
from langchain_huggingface import HuggingFacePipeline
from langchain.schema import HumanMessage

# Create the base LLM first
llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    model_kwargs={"temperature": 0.7},
    pipeline_kwargs={"max_new_tokens": 512}
)

# Then create the chat model
model = ChatHuggingFace(llm=llm)

# Ask a single question
response = model.invoke([HumanMessage(content="who is Donald trump?")])
print(response.content)
