from langchain.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings

def save_vector_store(chunks, path="faiss_index"):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(chunks, embedding=embeddings)
    vector_store.save_local(path)

def load_vector_store(path="faiss_index"):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    return FAISS.load_local(path, embeddings)
