from flask import Flask, render_template, request, jsonify
import os
from generate_explanations import process_single_image_sync
from werkzeug.utils import secure_filename
import nest_asyncio
import json
from radedu import radedu_geri_bildirim_interaktif

nest_asyncio.apply()

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max-limit
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}

# Upload klasörünü oluştur
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/doctor')
def doctor():
    return render_template('doctor_mode.html')

@app.route('/student', methods=['GET', 'POST'])
def student():
    if request.method == 'POST':
        student_text = request.form.get('student_text')
        dogru_cevap = request.form.get('dogru_cevap', '')
        image = request.form.get('image', '')

        try:
            feedback = radedu_geri_bildirim_interaktif(student_text)
        except Exception as e:
            feedback = f"🤖 Cevabınız alındı: {len(student_text)} karakter. Sistem geçici olarak kullanılamıyor."
        
        # Case bilgilerini yeniden oluştur
        case = {
            'image': image,
            'dogru_cevap': dogru_cevap
        }

        return render_template('student_mode.html',
                             case=case,
                             ogrenci_cevap=student_text,
                             feedback=feedback)

    return render_template('student_mode.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'Dosya yüklenmedi'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Dosya seçilmedi'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        try:
            result = process_single_image_sync(filepath)
            return jsonify(result)
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    return jsonify({'error': 'İzin verilmeyen dosya tipi'}), 400

@app.route('/egitim')
def egitim():
    try:
        with open("aciklamalar.json", encoding="utf-8") as f:
            data = json.load(f)

        valid_cases = []
        for case in data:
            if not case.get("llm_explanation", "").startswith("HATA:"):
                valid_cases.append(case)

        if not valid_cases:
            return "Geçerli vaka bulunamadı. <a href='/'>Ana Sayfaya Dön</a>"

        import random
        case_data = random.choice(valid_cases)

        # Encoding düzeltme fonksiyonu
        def fix_encoding(text):
            replacements = {
                'Ã§': 'ç', 'ÃŸ': 'ş', 'Ä±': 'ı', 'Ã¼': 'ü',
                'Ã¶': 'ö', 'ÄŸ': 'ğ', 'Ä°': 'İ', 'Ã‡': 'Ç',
                'ÅŸ': 'ş', 'â€': '"', 'â€™': "'"
            }
            for old, new in replacements.items():
                text = text.replace(old, new)
            return text

        tumor_names = {
            'meningioma': 'Meninjioma',
            'glioma': 'Glioma',
            'pituitary-tumor': 'Hipofiz Tümörü'
        }

        tumor_display = tumor_names.get(case_data['tumor_type'], case_data['tumor_type'].title())

        case = {
            "image": case_data["filename"],
            "clinical_info": f"🏥 Vaka Bilgileri:\n\nTümör Tipi: {tumor_display}\nBoyut: {case_data['size_cm']} cm\n\nLütfen bu MR görüntüsünü değerlendirip radyolojik bulgularınızı yazınız.",
            "dogru_cevap": fix_encoding(case_data["llm_explanation"]),
            "tumor_type": case_data["tumor_type"],
            "size_cm": case_data["size_cm"],
            "title": f"{tumor_display} Vakası"
        }

        return render_template("student_mode.html", case=case)

    except json.JSONDecodeError as e:
        return f"JSON dosyası okuma hatası: {str(e)}<br><a href='/'>Ana Sayfaya Dön</a>"        
    except Exception as e:
        return f"Beklenmeyen hata: {str(e)}<br><a href='/'>Ana Sayfaya Dön</a>"

@app.route('/evaluate', methods=["POST"])
def evaluate():
    ogrenci_cevap = request.form["ogrenci_cevap"]
    dogru_cevap = request.form["dogru_cevap"]
    image = request.form["image"]

    geri_bildirim = radedu_geri_bildirim_interaktif(ogrenci_cevap)

    return render_template("student_mode.html",
        case={"image": image, "dogru_cevap": dogru_cevap},
        ogrenci_cevap=ogrenci_cevap,
        geri_bildirim=geri_bildirim
    )

if __name__ == '__main__':
    app.run(debug=True, threaded=True)