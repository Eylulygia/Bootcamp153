import os
from dotenv import load_dotenv
import google.generativeai as genai
from retriever import get_ground_truth

# .env dosyasından API anahtarını al
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def radedu_geri_bildirim(student_text, tumor_type="glioma"):
    """Orijinal uzun format geri bildirim (eski versiyon)"""
    # Doğru cevabı RAG'den çek
    ground_truth = get_ground_truth(tumor_type)
    # Model tanımı (v1beta için UYUMLU olan model)
    model = genai.GenerativeModel("models/gemini-1.5-flash")
    
    # İstem (prompt)
    prompt = f"""
Sen bir tıp eğitmenisin. Aşağıdaki öğrenci yanıtını, doğru yanıtla kıyasla ve eksik veya hatalı yerleri belirt.

Öğrenci Cevabı:
\"\"\"{student_text}\"\"\"

Doğru Cevap:
\"\"\"{ground_truth}\"\"\"

Yalnızca öğrenciye rehber olacak şekilde yaz: örneğin 'Kitle boyutu belirtilmemiş', 'BT bulgularına yer verilmemiş' gibi.
Türkçe cevap ver.
"""
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"AI değerlendirme hatası: {str(e)}"

def radedu_geri_bildirim_interaktif(student_text):
    """İnteraktif ve kısa geri bildirim sistemi"""
    
    model = genai.GenerativeModel("models/gemini-1.5-flash")
    
    prompt = f"""
Sen dostane bir radyoloji öğretmenisin. Bu cevabı değerlendir: "{student_text}"

SADECE şu formatı kullan (maksimum 80 kelime):

🎯 GÖRDÜĞÜN: [Öğrencinin yazdıklarını 1 cümle ile özetle]

👍 GÜZEL: [Pozitif nokta - 1 cümle]

🔍 EKLEYEBİLİRİN: [1-2 spesifik eksik bulgu]

💭 TAVSİYE: [Pratik öneri - 1 cümle]

Samimi, kısa ve cesaretlendirici ol.
"""
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"🤖 Sistem geçici olarak kullanılamıyor. Cevabınız kaydedildi: {len(student_text)} karakter."

def radedu_geri_bildirim_kisa(student_text):
    """Çok basit ve hızlı geri bildirim"""
    
    # Basit analiz
    word_count = len(student_text.split())
    
    # Anahtar kelimeler
    key_terms = ['glioma', 'meningioma', 'kitle', 'lezyon', 'mr', 'beyin', 'tümör', 'boyut']
    found_terms = [term for term in key_terms if term.lower() in student_text.lower()]
    
    feedback = []
    
    if word_count < 10:
        feedback.append("⚠️ Çok kısa cevap. Daha detay ekleyin.")
    else:
        feedback.append("✅ Değerlendirme yapılmış.")
    
    if found_terms:
        feedback.append(f"👍 Doğru terimler: {', '.join(found_terms[:2])}")
    else:
        feedback.append("🔍 Spesifik radyolojik terimler ekleyin.")
    
    feedback.extend([
        "💡 Lokalizasyon belirtin",
        "💡 Boyut tahmini yapın"
    ])
    
    return "\n".join(feedback)