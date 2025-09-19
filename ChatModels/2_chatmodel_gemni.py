from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

print("Loading .env...")
load_dotenv()

print("Google API Key Loaded?", bool(os.getenv("GOOGLE_API_KEY")))

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)

print("Invoking model...")
try:
    result = model.invoke("Who is India's supreme god?")
    print("Response object:", result)
    print("Response content:", getattr(result, "content", "No content field"))
except Exception as e:
    print("Error occurred:", e)
