from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

prompt = ChatPromptTemplate.from_messages([
    ("system","reply in the mood of the user"),
    ("user","user mood : {mood}. Respond accordingly")
])
chat_model = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.4)

mood=input("Hi this is MoodBot, how are you feeling today:")

response = chat_model.invoke(prompt.format_messages(mood=mood))

print(response.content)
