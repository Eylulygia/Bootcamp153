import os
import json
from PIL import Image
import time
import google.generativeai as genai
from dotenv import load_dotenv
from retriever import get_info_from_rag
from ultralytics import YOLO
import asyncio

# .env'den API Key'i yükle
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("models/gemini-1.5-flash")

# YOLO model yolu kontrolü
MODEL_PATH = "best.pt"
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(
        f"YOLO model dosyası bulunamadı: {MODEL_PATH}\n"
        "Lütfen eğitilmiş model dosyasını (best.pt) projenin ana dizinine koyun."
    )

# YOLO modelini yükle
try:
    yolo_model = YOLO(MODEL_PATH)
except Exception as e:
    raise Exception(f"YOLO model yüklenirken hata oluştu: {str(e)}")

# Ayar
pixel_spacing_mm = 0.5

def pixel_to_cm(px, spacing_mm=pixel_spacing_mm):
    return round(px * spacing_mm / 10, 1)

def build_prompt(size_cm, tumor_type, knowledge_text, region="beyin"):
    return f"""
Beyin MR görüntüsünde {region} bölgesinde yaklaşık {size_cm} cm çapında bir lezyon (tümör) saptanmıştır. 
Görüntü işleme modeline göre bu lezyon {tumor_type.replace('-', ' ')} sınıfında yer almaktadır.

Aşağıda bu tümör tipi hakkında bilgi tabanından alınan içerik sunulmuştur:
---
{knowledge_text}
---

Lütfen aşağıdaki maddeleri kapsayan kısa, sade ve eğitici bir tıbbi açıklama üret:

1. Olası tümör tipi
2. Klinik önemi
3. Önerilen ileri tetkik ve tedavi yaklaşımları

Cevap 2-3 paragraflık açık anlatımlı bir metin olsun.
"""

async def process_single_image(image_path):
    # Görüntü dosyası kontrolü
    if not os.path.exists(image_path):
        return {"hata": f"Görüntü dosyası bulunamadı: {image_path}"}

    try:
        results = yolo_model(image_path)
    except Exception as e:
        return {"hata": f"YOLO analizi sırasında hata: {str(e)}"}

    if not results or not results[0].boxes:
        return {"hata": "Tümör tespit edilemedi."}

    try:
        # İlk kutuyu al
        box = results[0].boxes[0]
        x1, y1, x2, y2 = box.xyxy[0].tolist()
        pixel_width = x2 - x1
        pixel_height = y2 - y1
        avg_px = (pixel_width + pixel_height) / 2
        size_cm = pixel_to_cm(avg_px)

        class_id = int(box.cls[0].item())
        tumor_type = yolo_model.names[class_id]

        # RAG & prompt
        try:
            knowledge_text = get_info_from_rag(tumor_type)
            prompt = build_prompt(size_cm, tumor_type, knowledge_text)

            print(f"🧠 {image_path}: {size_cm} cm | {tumor_type} → AI açıklama alınıyor...")

            # Senkron çağrı kullan
            response = model.generate_content(prompt)
            explanation = response.text.strip()
        except Exception as e:
            explanation = f"Açıklama üretilirken hata oluştu: {str(e)}"

        result = {
            "filename": os.path.basename(image_path),
            "tumor_type": tumor_type,
            "size_cm": size_cm,
            "llm_explanation": explanation
        }

        return result
    except Exception as e:
        return {"hata": f"İşlem sırasında beklenmeyen hata: {str(e)}"}

# Senkron wrapper fonksiyon
def process_single_image_sync(image_path):
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(process_single_image(image_path))

# Örnek kullanım
if __name__ == "__main__":
    image_path = "upload.jpg"  # Doktorun yüklediği görsel
    result = process_single_image_sync(image_path)

    # Terminale yaz
    print(json.dumps(result, indent=2, ensure_ascii=False))

    # İstersen dosyaya da kaydet
    with open("aciklama_tek.json", "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
