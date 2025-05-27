import os
import zipfile
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import folium

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix

# --- 1. ZIP DOSYASINI AÇ ---
zip_path = "archive.zip"  # ZIP dosyasının yolu
extract_path = "unzipped_data"

# ZIP dosyasını çıkart
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)

# Çıkarılan dosyaları kontrol et
for root, dirs, files in os.walk(extract_path):
    for name in files:
        print(os.path.join(root, name))

# --- 2. CSV DOSYASINI OKU ---
csv_file = os.path.join(extract_path, "turkey_earthquakes(1915-2023_may).csv")
df = pd.read_csv(csv_file)

# --- 3. VERİ TEMİZLEME ---
df_clean = df[["Olus tarihi", "Olus zamani", "Enlem", "Boylam", "Derinlik", "Mw", "Yer"]].copy()
df_clean.columns = ["date", "time", "latitude", "longitude", "depth_km", "magnitude", "location"]
df_clean.dropna(subset=["magnitude"], inplace=True)

df_clean["datetime"] = pd.to_datetime(df_clean["date"].astype(str) + " " + df_clean["time"].astype(str), errors='coerce')
df_clean["year"] = df_clean["datetime"].dt.year

def magnitude_class(mag):
    if mag < 4.0:
        return "Küçük"
    elif mag <= 6.0:
        return "Orta"
    else:
        return "Büyük"

df_clean["magnitude_class"] = df_clean["magnitude"].apply(magnitude_class)

# --- 4. KEŞİFSEL ANALİZ ---
map = folium.Map(location=[39.0, 35.0], zoom_start=6)
for _, row in df_clean.head(500).iterrows():
    folium.CircleMarker(
        location=(row["latitude"], row["longitude"]),
        radius=row["magnitude"] * 0.8,
        popup=f"{row['location']} - {row['magnitude']}",
        color="crimson" if row["magnitude"] >= 6 else "blue",
        fill=True, fill_opacity=0.6
    ).add_to(map)
map.save("deprem_haritasi.html")

plt.figure(figsize=(8,5))
sns.scatterplot(data=df_clean, x="depth_km", y="magnitude", hue="magnitude_class", palette="Set1")
plt.title("Derinlik vs. Deprem Büyüklüğü")
plt.xlabel("Derinlik (km)")
plt.ylabel("Büyüklük (Mw)")
plt.tight_layout()
plt.show()

df_clean["city"] = df_clean["location"].str.extract(r"\(([^)]+)\)", expand=False)
top_cities = df_clean["city"].value_counts().head(10)
top_cities.plot(kind="bar", figsize=(10,5), color="darkcyan")
plt.title("En Çok Deprem Yaşanan 10 Şehir")
plt.ylabel("Deprem Sayısı")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# --- 5. MODELLEME ---
features = df_clean[["latitude", "longitude", "depth_km"]]
target = df_clean["magnitude_class"]

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.25, stratify=target, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

models = {
    "Random Forest": RandomForestClassifier(random_state=42, class_weight="balanced"),
    "KNN": KNeighborsClassifier(),
    "Decision Tree": DecisionTreeClassifier(random_state=42, class_weight="balanced")
}

results = {}
conf_matrices = {}

for name, model in models.items():
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)
    print(f"\n=== {name} Sınıflandırma Raporu ===")
    print(classification_report(y_test, y_pred))
    conf_matrices[name] = confusion_matrix(y_test, y_pred)

    scores = cross_val_score(model, X_train_scaled, y_train, cv=5, scoring='f1_macro')
    results[name] = {
        "F1_macro_mean": scores.mean(),
        "F1_macro_std": scores.std()
    }

# --- 6. KARMAŞIKLIK MATRİSLERİ ---
for name, cm in conf_matrices.items():
    plt.figure(figsize=(5,4))
    sns.heatmap(cm, annot=True, fmt="d", cmap="YlGnBu",
                xticklabels=models["Random Forest"].classes_,
                yticklabels=models["Random Forest"].classes_)
    plt.title(f"{name} - Confusion Matrix")
    plt.xlabel("Tahmin")
    plt.ylabel("Gerçek")
    plt.tight_layout()
    plt.show()

# --- 7. MODEL PERFORMANS ÖZETİ ---
results_df = pd.DataFrame(results).T
print("\n=== Model Performans Özeti ===")
print(results_df)

best_model = results_df["F1_macro_mean"].idxmax()
worst_model = results_df["F1_macro_mean"].idxmin()

print(f"\n En iyi ortalama F1 skoru '{best_model}' modeline aittir.")
print(f" En düşük ortalama F1 skoru '{worst_model}' modeline aittir.")

print("\n Yorum:")
print(f"• {best_model} modeli, sınıflar arasında daha dengeli bir performans göstermiştir.")
print(f"• {worst_model} modeli ise daha az başarılı olmuştur, özellikle 'Orta' gibi sınıflarda hata yapmıştır.")
