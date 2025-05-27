# Türkiye Depremleri Veri Bilimi Projesi

Bu projede, 1915–2023 yılları arasında Türkiye’de gerçekleşen depremler veri bilimi teknikleriyle analiz edilmiştir.  
Projenin temel amacı, depremlerin yapısal özelliklerini (enlem, boylam, derinlik) kullanarak deprem büyüklüğünü tahmin edebilecek bir makine öğrenmesi modeli geliştirmektir.

---

## 🎯 Projenin Amacı

Depremlerin konumsal ve yapısal verilerini analiz ederek:
- Veri seti üzerindeki genel dağılımları ortaya koymak (keşifsel veri analizi),
- Türkiye’de deprem yoğunluğunu coğrafi olarak görselleştirmek,
- Deprem büyüklüklerini “Küçük”, “Orta” ve “Büyük” sınıflarına ayırmak,
- Bu sınıfları tahmin edebilecek sınıflandırma modelleri oluşturmak amaçlanmıştır.

---

## 📁 Veri Seti

- **Kaynak:** Kaggle – “Turkey Earthquakes 1915–2023 May” (Oğuzhan Bal)
- **Kayıt Sayısı:** ~20.000 satır
- **Sütunlar:** Tarih, saat, enlem, boylam, derinlik, büyüklük (Mw), yer bilgisi
- **Kullanılan Dosya:** `archive.zip` içinde `turkey_earthquakes(1915-2023_may).csv`

---

## 🧪 Kullanılan Yöntemler

### 📌 Veri Ön İşleme
- Sadece gerekli sütunlar seçildi: tarih, saat, enlem, boylam, derinlik, Mw, yer
- Eksik değer içeren satırlar (özellikle Mw olmayanlar) çıkarıldı
- Tarih ve saat birleştirilerek `datetime` formatı oluşturuldu
- Mw değerine göre sınıflandırma yapıldı:
  - Küçük: Mw < 4.0
  - Orta: 4.0 ≤ Mw ≤ 6.0
  - Büyük: Mw > 6.0

### 📊 Görselleştirme
- `matplotlib`, `seaborn` ve `folium` kullanılarak:
  - Derinlik ve büyüklük scatter plot
  - En çok deprem olan şehirlerin bar grafiği
  - 500 büyük depremin interaktif harita üzerinde gösterimi (`deprem_haritasi.html`)

### 🧠 Makine Öğrenmesi
- Özellikler: `latitude`, `longitude`, `depth_km`
- Hedef: `magnitude_class` (Küçük, Orta, Büyük)
- Veri eğitim/test (%75/%25) olarak ayrıldı
- `StandardScaler` ile öznitelik ölçeklendi
- Kullanılan Modeller:
  - Random Forest (class_weight=‘balanced’)
  - K-Nearest Neighbors (KNN)
  - Decision Tree (class_weight=‘balanced’)
- Değerlendirme metrikleri:
  - `classification_report`, `confusion_matrix`, `cross_val_score` (F1-macro)

---

## 📈 Özet Sonuçlar

- **Random Forest** modeli, en yüksek ortalama F1 skorunu verdi
- KNN modeli daha basit yapısıyla orta seviyede performans sağladı
- Decision Tree, özellikle “Büyük” deprem sınıfında düşük başarı gösterdi
- En çok tahmin hatası, sınıf dağılımının dengesizliğinden dolayı “Orta” sınıfta gözlendi
- Coğrafi görselleştirme sayesinde Türkiye’de deprem açısından riskli bölgeler kolayca tespit edildi

---

## 📂 Proje Dosyaları

| Dosya | Açıklama |
|-------|----------|

| `earthquake_analysis.py` | Python script – notebook alternatifi |
| `archive.zip` | Ham veri seti ZIP formatında |
| `deprem_haritasi.html` | Folium ile oluşturulmuş interaktif harita |


---

## ⚙️ Kullanılan Kütüphaneler

- `pandas`, `numpy` – veri işleme
- `matplotlib`, `seaborn` – görselleştirme
- `folium` – harita çizimi
- `scikit-learn` – modelleme ve değerlendirme

---

## 👩‍💻 Katkıda Bulunanlar

- Ezgi Sarıhan  
- Merve Karakuş

---



