# Türkiye Depremleri Veri Bilimi Projesi

Bu proje, 1915–2023 yılları arasında Türkiye’de meydana gelen depremleri analiz etmeyi ve bu depremleri büyüklüklerine göre sınıflandırmayı amaçlamaktadır. Veri bilimi araçları ve makine öğrenmesi algoritmaları kullanılarak kapsamlı bir analiz yapılmıştır.

## 🔍 Projenin Amacı

Depremlerin **enlem, boylam ve derinlik** bilgilerini kullanarak büyüklük sınıfını ("Küçük", "Orta", "Büyük") tahmin eden bir sınıflandırma modeli oluşturmak.

## 🧾 Kullanılan Veriler

- **Veri seti:** 1915-2023 arası Türkiye depremleri (Kaynak: Kaggle – Oğuzhan Bal)
- **Dosya:** `archive.zip` → içindeki CSV dosyası kodda otomatik açılır
- **Özellikler:** Enlem, boylam, derinlik, tarih, saat, büyüklük (Mw)

## 🧪 Kullanılan Araçlar ve Kütüphaneler

- Python (pandas, numpy, matplotlib, seaborn)
- Folium (coğrafi harita görselleştirme)
- scikit-learn (RandomForest, KNN, DecisionTree, ölçekleme, cross-validation)

## 🧹 Veri Temizleme

- Eksik büyüklük değerleri çıkarıldı
- Tarih ve saat `datetime` formatına dönüştürüldü
- "Küçük", "Orta", "Büyük" sınıfları oluşturuldu

## 📊 Görselleştirme

- Derinlik vs. büyüklük dağılım grafiği
- En çok deprem olan şehirlerin bar grafiği
- `deprem_haritasi.html` dosyasında Folium haritası

## 🧠 Makine Öğrenmesi

Üç farklı model kullanıldı ve karşılaştırıldı:
- Random Forest ✅ (en iyi performans)
- K-Nearest Neighbors
- Decision Tree

### 🎯 En iyi sonuç:
**Random Forest**, `F1_macro` ortalamasında en yüksek başarıyı verdi. Özellikle “Orta” büyüklükteki depremleri yüksek doğrulukla tahmin etti.

## 📂 Proje Dosyaları

| Dosya | Açıklama |
|-------|----------|
| `VeriBilimiProjesi.ipynb` | Jupyter Notebook – tüm analiz ve görselleştirme burada |
| `earthquake_analysis.py` | Alternatif Python script versiyonu |
| `archive.zip` | Ham veri dosyasını içerir (otomatik açılır) |
| `deprem_haritasi.html` | İnteraktif deprem haritası |
| `VeriBilimiGrup7_Sunum.pdf` | 

## 👩‍💻 Katkıda Bulunanlar

- Ezgi Sarıhan  
- Merve Karakuş
