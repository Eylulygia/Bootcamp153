from langchain_community.vectorstores import Chroma
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

def get_info_from_rag(query: str, top_k=2) -> str:
    embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=api_key) 
    db = Chroma(persist_directory="rag_chroma", embedding_function=embedding)
    docs = db.similarity_search(query, k=top_k)
    return "\n".join([doc.page_content for doc in docs])

def get_ground_truth(tumor_type):
    try:
        if tumor_type == "glioma":
            return open("knowledge/glioma.txt", "r", encoding="utf-8").read()
        elif tumor_type == "meningioma":
            return open("knowledge/meningioma.txt", "r", encoding="utf-8").read()
        elif tumor_type == "pituitary":
            return open("knowledge/pituitary-tumor.txt", "r", encoding="utf-8").read()
        return "Etiketlenmiş veri bulunamadı."
    except Exception as e:
        return f"Dosya okuma hatası: {str(e)}"