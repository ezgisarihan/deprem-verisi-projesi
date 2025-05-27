<h1 align="center">🌍 Türkiye Depremleri Veri Analizi ve Sınıflandırma</h1>

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/e/e8/Turkey_location_map.svg" width="300"/>
</p>

---

## 🔎 Proje Hakkında

Bu proje, 1915–2023 yılları arasında Türkiye’de meydana gelen depremleri veri bilimi teknikleriyle analiz etmek ve bu verileri kullanarak bir sınıflandırma modeli geliştirmek amacıyla gerçekleştirilmiştir. Çalışmanın odak noktası, depremlerin **enlem**, **boylam** ve **derinlik** bilgilerini temel alarak **deprem büyüklüğünü ("Küçük", "Orta", "Büyük") tahmin edebilecek bir model** inşa etmektir.

---

## 🎯 Proje Amacı

🔸 Türkiye’de meydana gelen tarihsel depremleri istatistiksel olarak analiz etmek  
🔸 Verileri temizleyip sınıflandırarak anlamlı görseller üretmek  
🔸 Depremlerin büyüklüklerini tahmin eden makine öğrenmesi modelleri geliştirmek  
🔸 Coğrafi olarak yoğunlukları görselleştirerek riskli bölgeleri belirlemek  

---

## 📊 Veri Seti Bilgileri

- **Kaynak:** [Kaggle - Turkey Earthquakes 1915-2023 May (Oğuzhan Bal)](https://www.kaggle.com/datasets/oguzhanbal/turkey-earthquakes-1915-2023-may)
- **Dosya:** `turkey_earthquakes(1915-2023_may).csv` (ZIP içinde)
- **Veri Formatı:** CSV
- **Satır Sayısı:** ~20.000
- **Sütunlar:** Tarih, saat, enlem, boylam, derinlik, büyüklük (Mw), yer

---

## 🧪 Kullanılan Yöntemler ve Süreçler

### 1. 📦 Veri Temizleme ve Ön İşleme

| Adım | Açıklama |
|------|----------|
| Eksik veriler | Büyüklük (Mw) bilgisi olmayan kayıtlar çıkarıldı |
| Tarih-Saat | `datetime` sütunu oluşturuldu |
| Hedef Sınıf | Büyüklük verisi 3 sınıfa ayrıldı: Küçük (<4), Orta (4–6), Büyük (>6) |
| Konum bilgisi | Yer sütunundan şehir adı çıkarıldı (`str.extract`) |

---

### 2. 📊 Keşifsel Veri Analizi

- Scatter Plot: Derinlik ve büyüklük arasındaki ilişki
- Bar Chart: En çok deprem yaşanan ilk 10 şehir
- Histogram: Büyüklük dağılımı
- Harita: `folium` kullanılarak 500 büyük depremin coğrafi gösterimi

📌 Örnek Harita:  
👉 [deprem_haritasi.html](./deprem_haritasi.html)

---

### 3. 🤖 Makine Öğrenmesi

| Aşama | Detay |
|-------|-------|
| Özellikler | latitude, longitude, depth_km |
| Hedef | magnitude_class |
| Modeller | Random Forest ✅, KNN, Decision Tree |
| Ölçekleme | StandardScaler |
| Performans | `classification_report`, `confusion_matrix`, `cross_val_score` (5-fold) |

---

### 🧠 Model Sonuçları

- **Random Forest:** En yüksek F1 macro skoru (%84 civarı), sınıflar arası dengeli tahmin  
- **KNN:** Basit ama etkili, küçük veri setlerinde başarılı  
- **Decision Tree:** Aşırı öğrenme riski, “Büyük” sınıfta daha zayıf performans

📊 Karmaşıklık matrisi ve F1 skorlarına göre en başarılı model **Random Forest** olmuştur.

---

## 🌐 Görselleştirme Örnekleri

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Seismic_hazard_map_Turkey.jpg/800px-Seismic_hazard_map_Turkey.jpg" width="500"/>
</p>

---

## 📂 Proje Dosyaları

| Dosya Adı | Açıklama |
|-----------|----------|
| `VeriBilimiProjesi.ipynb` | Jupyter Notebook – analiz, modelleme, grafik |
| `earthquake_analysis.py` | Python script – tek dosyada tüm süreç |
| `archive.zip` | Ham veri içeren ZIP |
| `deprem_haritasi.html` | Harita tabanlı görselleştirme (Folium) |
| `VeriBilimiGrup7_Sunum.pdf` | 
---
## ⚙️ Kullanılan Kütüphaneler

- `pandas`, `numpy` – veri işleme
- `matplotlib`, `seaborn` – görselleştirme
- `folium` – harita çizimi
- `scikit-learn` – modelleme ve değerlendirme

