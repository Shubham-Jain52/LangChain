from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import load_prompt
import streamlit as st
load_dotenv()

chat_model = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)

st.header("researchBuddy")

paper_type = st.selectbox("Select the type of research paper you are interested in:", 
                          ("Survey Paper", "Experimental Paper", "Theoretical Paper", "Review Paper", "Case Study"))
details_type = st.selectbox("Select the level of detail you want in the response:",(
    "High-level Overview", "In-depth Analysis", "Step-by-step Explanation", "Concise Summary"
))

user_query = st.selectbox("select you research topic here:",("Artificial Intelligence", "Machine Learning", "Natural Language Processing", "Computer Vision", "Robotics", "Data Science", "Cybersecurity", "Cloud Computing", "Internet of Things", "Blockchain Technology"))   

# Making template:
template = load_prompt("template.json")

prompt=template.invoke({
    "paper_type": paper_type,
    "details_type": details_type,
    "user_query": user_query
})


if user_query and paper_type and details_type:
    if st.button("Get Response"):
        response = chat_model.invoke(prompt)
        st.write(response.content)