import os
from langchain_groq import ChatGroq
from langchain.schema import HumanMessage
from dotenv import load_dotenv

# Load API Key
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Initialize Groq LLM
chat_model = ChatGroq(model_name="llama3-8b-8192", groq_api_key=api_key)


# Test Prompt
response = chat_model([HumanMessage(content="What is an agency?")])
print("\n🤖 Groq Response:", response.content)
