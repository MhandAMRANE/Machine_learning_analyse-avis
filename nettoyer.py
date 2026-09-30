from src.data_loader import load_reviews
from src.preprocessing import clean_text, prepare_dataset

print("=== Test sur des phrases ===")
exemples = [
    "Film GÉNIAL !!! <br/>Vu le 12/03, à voir absolument : https://allocine.fr",
    "Ce film n'est PAS bon... vraiment décevant.",
]
for phrase in exemples:
    print("Avant :", phrase)
    print("Après :", clean_text(phrase))
    print()

print("=== Nettoyage du jeu complet ===")
df = load_reviews()
print("Avant :", len(df), "avis")
df = prepare_dataset(df)
print("Après :", len(df), "avis")

print("\n=== Exemple réel ===")
print("Original :", df.loc[0, "avis"][:200])
print("Nettoyé  :", df.loc[0, "avis_propre"][:200])