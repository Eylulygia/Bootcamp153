import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

models = genai.list_models()
for model in models:
    print(f"🧠 {model.name} | supports: {model.supported_generation_methods}")
