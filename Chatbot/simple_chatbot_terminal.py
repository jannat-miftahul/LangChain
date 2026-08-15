from langchain_groq import ChatGroq
from dotenv import load_dotenv 
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage


load_dotenv()

llm = ChatGroq(model="llama-3.3-70b-versatile")

chat_history = [SystemMessage(content="You are a helpful assistant. Always Answer in a short paragraph(1-2 Sentence)")]

# chatbot 
while True:
    user_input = input('You :')

    chat_history.append(HumanMessage(content=user_input))

    if user_input == 'exit':
        break

    result = llm.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI : ", result.content)

print("Printing chat history", chat_history)