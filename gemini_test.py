import google.generativeai as genai
from dotenv import load_dotenv
import os

# 1. .env dosyasını yükle
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# 2. API yapılandırması
genai.configure(api_key=api_key)

# 3. Model bağlantısı
try:
    model = genai.GenerativeModel("models/gemini-pro")
    prompt = "Merhaba, nasılsın?"
    response = model.generate_content(prompt)
    print("✅ API başarılı çalışıyor. Model yanıtı:")
    print(response.text)
except Exception as e:
    print("❌ Bir hata oluştu:")
    print(e)
