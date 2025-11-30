from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedd = HuggingFaceEndpointEmbeddings(
    repo_id="sentence-transformers/all-MiniLM-L6-v2",
    task="feature-extraction",
)

def compute_doc_similarities(doc_list,user_doc):
    results_docs = embedd.embed_documents(doc_list)
    results_user = embedd.embed_query(user_doc)
    similarities = cosine_similarity(results_docs, np.array(results_user).reshape(1, -1))
    return similarities


docs = [
    "japan is a beautiful country with a rich cultural heritage.",
    "the capital of france is paris, known for its art, fashion, and landmarks.",
    "machine learning is a subset of artificial intelligence focused on data-driven predictions.",
    "the great wall of china is one of the most famous historical structures in the world.",
    "python is a versatile programming language used for web development, data analysis, and more.",
    "the amazon rainforest is the largest tropical rainforest on earth, home to diverse wildlife.",
    "the theory of relativity was developed by albert einstein and revolutionized physics.",
    "the nile river is the longest river in the world, flowing through northeastern africa.",
]

user_input = input("Enter a document to compare: \n")

similarity_scores = compute_doc_similarities(docs, user_input)

try:
    max_score = 0
    for i, score in enumerate(similarity_scores):
        if score > max_score:
            max_score = score
            most_similar_doc = docs[i]
    print("Most similar document:\n", most_similar_doc)
except NameError:
    most_similar_doc = "No similar document found."
    print(most_similar_doc)