<h1 align="center"> Türkiye Depremleri Veri Analizi ve Sınıflandırma Projesi</h1>

---

## Proje Hakkında

Bu proje, 1915–2023 yılları arasında Türkiye’de meydana gelen depremleri veri bilimi teknikleriyle analiz etmek ve bu verileri kullanarak bir sınıflandırma modeli geliştirmek amacıyla gerçekleştirilmiştir. Çalışmanın odak noktası, depremlerin **enlem**, **boylam** ve **derinlik** bilgilerini temel alarak **deprem büyüklüğünü ("Küçük", "Orta", "Büyük") tahmin edebilecek bir model** inşa etmektir.

## Proje Amacı

- Türkiye’de meydana gelen tarihsel depremleri istatistiksel olarak analiz etmek  
- Verileri temizleyip sınıflandırarak anlamlı görseller üretmek  
- Depremlerin büyüklüklerini tahmin eden makine öğrenmesi modelleri geliştirmek  
- Coğrafi olarak yoğunlukları görselleştirerek riskli bölgeleri belirlemek

---

##  Veri Seti Bilgileri

- **Kaynak:** [Kaggle - Turkey Earthquakes 1915-2023 May (Oğuzhan Bal)](https://www.kaggle.com/datasets/oguzhanbal/turkey-earthquakes-1915-2023-may)
- **Dosya:** `turkey_earthquakes(1915-2023_may).csv` (ZIP içinde)
- **Veri Formatı:** CSV
- **Satır Sayısı:** ~20.000
- **Sütunlar:** Tarih, saat, enlem, boylam, derinlik, büyüklük (Mw), yer

---

##  Kullanılan Yöntemler ve Süreçler

### 1. Veri Temizleme ve Ön İşleme

| Adım | Açıklama |
|------|----------|
| Eksik veriler | Büyüklük (Mw) bilgisi olmayan kayıtlar çıkarıldı |
| Tarih-Saat | `datetime` sütunu oluşturuldu |
| Hedef Sınıf | Büyüklük verisi 3 sınıfa ayrıldı: Küçük (<4), Orta (4–6), Büyük (>6) |
| Konum bilgisi | Yer sütunundan şehir adı çıkarıldı (`str.extract`) |

---

## Keşifsel Veri Analizi

Veri setinde deprem büyüklüğü ve derinliği arasındaki ilişki scatter plot ile incelendi.  
En çok deprem yaşanan şehirler bar grafik ile görselleştirildi.  
Bu sayede Türkiye’deki deprem yoğunluğu daha net şekilde ortaya kondu.

---

##  Görselleştirme

Folium kütüphanesi ile 500 büyük depremin yer aldığı interaktif harita oluşturuldu.  
Matplotlib ve seaborn ile grafikler hazırlandı.  
Bu görseller analiz sonuçlarının daha anlaşılır olmasını sağladı.

---

## Makine Öğrenmesi

Enlem, boylam ve derinlik bilgileriyle deprem büyüklüğü sınıflandırıldı.  
Random Forest, KNN ve Decision Tree modelleri karşılaştırıldı.  
En iyi sonucu Random Forest verdi.  
Modeller `F1 skoru`, `confusion matrix` ve `cross-validation` ile değerlendirildi.

---
##  Model Sonuçları

Makine öğrenmesi modelleri arasında en başarılı sonuç, Random Forest algoritması ile elde edilmiştir.  
Bu model, sınıflar arası dengesizliğe rağmen yüksek F1-macro skoru ile öne çıkmıştır.

KNN (K-Nearest Neighbors) modeli orta düzeyde performans sergilemiş, özellikle küçük deprem sınıflarında kabul edilebilir sonuçlar üretmiştir.

Decision Tree modeli ise daha basit bir yapıya sahip olmasına rağmen özellikle "Büyük" deprem sınıfında düşük başarı göstermiştir.

Modellerin başarı düzeyi; doğruluk, F1 skoru, çapraz doğrulama ve karmaşıklık matrisi gibi değerlendirme metrikleriyle analiz edilmiştir.  
Sonuçlar, Random Forest modelinin sınıflandırma görevinde en güvenilir seçenek olduğunu göstermektedir.

---

##  Kullanılan Kütüphaneler

```bash
- pandas
- numpy
- matplotlib, seaborn
- folium
- scikit-learn



