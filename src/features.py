"""Transformation des textes en nombres (TF-IDF)."""
from sklearn.feature_extraction.text import TfidfVectorizer


def build_vectorizer() -> TfidfVectorizer:
    """Crée le transformateur TF-IDF (pas encore entraîné)."""
    return TfidfVectorizer(
        ngram_range=(1, 2),
        min_df=5,
        max_df=0.9,
        max_features=50_000,
        sublinear_tf=True,
    )