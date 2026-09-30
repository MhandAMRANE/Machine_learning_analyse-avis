from src.data_loader import load_reviews

df = load_reviews()

print("=== Taille du jeu ===")
print(df.shape)

print("\n=== Trois exemples ===")
for _, ligne in df.head(3).iterrows():
    print(f"[label {ligne['label']}] {ligne['avis'][:150]}...")

print("\n=== Répartition positif / négatif ===")
print(df["label"].value_counts(normalize=True).round(3))

print("\n=== Valeurs manquantes ===")
print(df.isna().sum())

print("\n=== Doublons ===")
print(df.duplicated(subset="avis").sum())

print("\n=== Longueur des avis (en mots) ===")
df["nb_mots"] = df["avis"].str.split().str.len()
print(df["nb_mots"].describe().round(1))