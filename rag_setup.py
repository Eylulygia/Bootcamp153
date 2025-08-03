from langchain_community.vectorstores import Chroma
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader
import os
from dotenv import load_dotenv

# Ortam değişkenlerini yükle
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# 1. Bilgi dosyalarını yükle (.txt dosyalarını klasörden oku)
loader = DirectoryLoader("knowledge", glob="*.txt")  # encoding kaldırıldı!
documents = loader.load()

# 2. Metinleri chunk'lara böl
splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=30)
docs = splitter.split_documents(documents)

# 3. Embedding hesapla ve vektör veritabanına aktar
embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=api_key)
db = Chroma.from_documents(docs, embedding, persist_directory="rag_chroma")
db.persist()

print("✅ RAG veritabanı başarıyla oluşturuldu.")
