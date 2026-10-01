from src.data_loader import load_reviews
from src.features import build_vectorizer
from src.preprocessing import prepare_dataset

df = prepare_dataset(load_reviews())

vectorizer = build_vectorizer()
X = vectorizer.fit_transform(df["avis_propre"])

print("=== La matrice ===")
print("Forme (avis, mots) :", X.shape)
remplissage = X.nnz / (X.shape[0] * X.shape[1])
print(f"Cases non nulles : {remplissage:.3%}")

print("\n=== Le vocabulaire ===")
print("Nombre de mots et paires :", len(vectorizer.vocabulary_))
for expression in ["pas bon", "très bon", "à voir", "chef d"]:
    print(f"'{expression}' présent ?", expression in vectorizer.vocabulary_)

print("\n=== Les mots les plus importants du premier avis ===")
print(df.loc[0, "avis_propre"][:200], "...")
mots = vectorizer.get_feature_names_out()
ligne = X[0]
top = sorted(zip(ligne.indices, ligne.data), key=lambda t: -t[1])[:8]
for index, score in top:
    print(f"  {mots[index]:<25} {score:.3f}")