from ultralytics import YOLO

# Boş bir YOLO modeli oluştur
model = YOLO('yolov8n.pt')

# Model sınıflarını güncelle
model.names = {
    0: 'glioma',
    1: 'meningioma',
    2: 'pituitary'
}

# Modeli kaydet
model.save('tumor-detector.pt')

print("✅ Örnek model oluşturuldu: tumor-detector.pt")