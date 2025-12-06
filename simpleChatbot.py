from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)

chat_history= []

while True:
    User_input = input("You: ")
    chat_history.append({"role": "user", "content": User_input})
    if User_input != "exit":
        response = model.invoke(chat_history)
        chat_history.append({"role": "bot", "content": response.content})
        print(f"Bot: {response.content}")
