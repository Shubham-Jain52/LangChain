from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    input_variables=["paper_type", "details_type", "user_query"],
    template="Provide a {details_type} on {user_query} in the form of a {paper_type}."  
)

template.save("template.json")