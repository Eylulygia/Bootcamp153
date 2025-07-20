# Bootcamp Grup 153

## Takım Üyeleri

- **Eylül Medine Kamar** : Developer  
- **Esra Gökce** : Developer 
- **Helin Yaren Batı** : Developer  
- **Tolga Kaya** : Product Owner  
- **Şevval Savaş** : Scrum Master 


---

## Görev Dağılımı

### Eylül Medine Kamar (AI/ML Engineer)
**Sorumluluklar:**
- Medical imaging datasets hazırlama ve preprocessing  
- Veri işaretleme (annotation) koordinasyonu  
- YOLOv8 model training ve fine-tuning  
- Training data quality control  
- Model performance evaluation  

### Esra Gökce (AI/ML Engineer)
**Sorumluluklar:**
- YOLOv8 model architecture optimization  
- Real-time inference pipeline  
- Bounding box koordinatları hesaplama  
- Model deployment ve serving  
- Performance monitoring ve optimization  

### Helin Yaren Batı (Full-Stack Developer)
**Sorumluluklar:**
- FastAPI ile API endpoints oluşturma  
- React ile kullanıcı arayüzü geliştirme  
- Dosya yükleme ve işleme  
- Database operations  
- Frontend-Backend integration  
- API documentation  

### Tolga Kaya (NLP Engineer & Project Owner)
**Sorumluluklar:**
- Gemini API integration  
- Prompt engineering (medical context)  
- RAG system implementation  
- Medical literature database hazırlama  
- Response quality assurance  

### Şevval Savaş (DevOps & Scrum Master)
**Sorumluluklar:**
- Deployment ve hosting  
- CI/CD pipeline kurulumu  
- Demo hazırlığı ve presentation  
- Documentation ve testing  
- External project coordination (diğer görevlerin)

---

## Ürün İsmi: **VEZİN**

### Ürün Açıklaması
**VEZİN**, röntgen ve MR gibi tıbbi görüntülerdeki anomalileri tespit edip, bu bulguları tıbbi dilde açıklayan bir web uygulamasıdır. Sistem, hem doktorlar için klinik destek sağlayarak hem de tıp öğrencilerinin eğitimine katkıda bulunarak sağlıkta yapay zeka ve eğitimde yapay zekayı aynı potada eritir.

### Ürünün Amacı
**Sorun:** Doktorların zamanla yarışarak onlarca görüntüye bakmak zorunda olması (günde 300+ hasta) → hata riski, dikkat dağınıklığı  
**Çözüm:** Otomatik anomali tespiti ve açıklaması → hızlı ön değerlendirme, eğitim desteği, ikincil görüş etkisi  
**Özgünlük:** Çoğu görüntüleme projesi sınıflandırmada kalırken, bu proje anlatma + eğitme boyutu ekliyor.

---

## Ürünün Özellikleri

### Doktor Modu
- **Otomatik Anomali Tespiti:** YOLO modeli ile görüntüdeki anormallikleri kutularla işaretleme  
- **Tıbbi Açıklama:** LLM (Gemini) ile tespit edilen anomalileri tıbbi dilde açıklama  
- **Görsellik:** Görüntü + kutular (vizüel) + açıklamalar (metinsel)  
- **Hızlı Ön Değerlendirme:** Doktorların iş yükünü azaltma  

### Öğrenci Modu (RADEDU Eğitim Sistemi)
- **Etkileşimli Öğrenme:** Öğrenciden önce cevap isteme  
- **Karşılaştırmalı Analiz:** Öğrenci cevabı ile doğru cevabı karşılaştırma  
- **Akıllı Geri Bildirim:** Gemini API ile detaylı değerlendirme  
- **Eğitimsel Açıklamalar:** Tıp eğitimi için özelleştirilmiş içerik  

---

## RAG + LLM Kombinasyonu

- **Kaynak Destekli Açıklamalar:** Fleischner Society 2017 rehberi gibi tıbbi kaynaklardan bilgi alma  
- **Kişiselleştirilmiş Yorumlama:** Doktor notu + görüntü kombinasyonu ile detaylı analiz  
- **Güncel Tıbbi Bilgi:** Sürekli güncellenen tıbbi literatür desteği  

---

## Hedef Kitle
- Doktorlar  
- Tıp Öğrencileri  
- Klinikler / Fakülteler  

---

## Sprint 1

### Sprint içinde tamamlanması tahmin edilen puan: **100 Puan**

**Puan tamamlama mantığı:**  
Toplamda proje boyunca tamamlanması gereken 300 puanlık backlog bulunmaktadır. 3 sprint'e bölündüğünde ilk sprintte 100 ile başlaması gerektiğine karar verildi.

---

### Daily Scrum
Daily Scrum toplantılarının zamansal sebeplerden ötürü **Whatsapp üzerinden** yapılmasına karar verilmiştir.  
Daily Scrum toplantısı örneği **`.jpeg` formatında Drive linki ile birlikte paylaşılacaktır.

[Google Meet Toplantı Ekran Görüntüleri](https://drive.google.com/drive/folders/1wCZDMRQ7IockN_D0YT-pZ2V6VZ-9cMXZ?usp=sharing)

[Whatsapp Ekran Görüntüleri](https://drive.google.com/drive/folders/1GR3ou2x0oFUVNIUA04mgGUNG7XnEPVQP?usp=sharing)


---

### Sprint Board Update
<img width="835" height="829" alt="Image" src="https://github.com/user-attachments/assets/e2ba4acd-d865-441a-a0f8-012bdc49f26c" />

---
### Ürünün Durumu
<img width="1015" height="576" alt="Image" src="https://github.com/user-attachments/assets/b0db15b7-aea5-495f-a48e-4018a9fee2d9" />
<img width="1016" height="570" alt="Image" src="https://github.com/user-attachments/assets/749f9249-9474-45e6-ade7-33e526f60482" />
<img width="1015" height="566" alt="Image" src="https://github.com/user-attachments/assets/071e192e-b665-42f1-8c65-683279068bf5" />
<img width="1002" height="563" alt="Image" src="https://github.com/user-attachments/assets/135331b8-e378-4ae5-9cce-27a1a36dabfe" />
<img width="899" height="504" alt="Image" src="https://github.com/user-attachments/assets/46c5efa6-7e8b-442f-b0f3-348fcebcc2bd" />
<img width="897" height="507" alt="Image" src="https://github.com/user-attachments/assets/2f9fc2dd-8a41-4cbf-97ee-5c187b7eeb7f" />
<img width="899" height="508" alt="Image" src="https://github.com/user-attachments/assets/c121db46-84c6-4280-acf7-2506f26e97fa" />


---
### Sprint Review

**Alınan Kararlar:**
- Ürünün sağlık alanında özellikle görüntü üzerine olacağına karar verildi.  
- Kullanılacak yapay zeka modelleri belirlendi.  
- Veri setleri incelenmeye ve seçilmeye başlandı.  
- Ürünün genel akışı ve teması belirlendi.  

---

### Sprint Retrospective

- Scrum Master ve Product Owner belirlenmiştir.  
- Görev dağılımı, takım üyelerinin ilgi alanlarına ve iş yüküne göre gerçekleştirilmiştir.
- İletişim etkin şekilde sürdürüldü ve toplantılara zamanında katınıldı.
- Toplantılar dışında Whatsapptan sürekli iletişim kuruldu.
- Projenin temel yapısı ve modülleri netleşti.

---

## Sprint 2

### Sprint içinde tamamlanması tahmin edilen puan: **100 Puan**

**Puan tamamlama mantığı:**  
Toplamda proje boyunca tamamlanması gereken 300 puanlık backlog bulunmaktadır. 3 sprint'e bölündüğünde ilk sprintte 100 ile başlaması gerektiğine karar verildi.

---

### Daily Scrum
Daily Scrum toplantılarının zamansal sebeplerden ötürü **Whatsapp üzerinden** yapılmasına karar verilmiştir.  
Daily Scrum toplantısı örneği **`.jpeg` formatında Drive linki ile birlikte paylaşılacaktır.

[Google Meet Toplantı Ekran Görüntüleri](https://drive.google.com/drive/folders/1wCZDMRQ7IockN_D0YT-pZ2V6VZ-9cMXZ?usp=sharing)

[Whatsapp Ekran Görüntüleri](https://drive.google.com/drive/folders/1GR3ou2x0oFUVNIUA04mgGUNG7XnEPVQP?usp=sharing)


---

### Sprint Board Update

---
### Ürünün Durumu


---
