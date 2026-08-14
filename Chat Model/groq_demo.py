# groq
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

# llm = ChatGroq(model="openai/gpt-oss-20b")
llm = ChatGroq(model="llama-3.3-70b-versatile")

result = llm.invoke("Write a poem about the ocean.")
print(result.content)