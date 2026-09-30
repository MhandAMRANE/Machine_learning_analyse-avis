"""Chargement du jeu de données d'avis."""
import pandas as pd

from src.config import DATA_DIR, DATASET_NAME, RANDOM_STATE, SAMPLE_SIZE

CACHE_FILE = DATA_DIR / "avis.csv"


def load_reviews() -> pd.DataFrame:
    """Retourne un tableau de SAMPLE_SIZE avis avec les colonnes 'avis' et 'label'."""
    if CACHE_FILE.exists():
        return pd.read_csv(CACHE_FILE)

    from datasets import load_dataset

    dataset = load_dataset(DATASET_NAME, split="train")
    df = dataset.to_pandas()
    df = df.rename(columns={"review": "avis"})
    df = df.sample(n=SAMPLE_SIZE, random_state=RANDOM_STATE).reset_index(drop=True)

    df.to_csv(CACHE_FILE, index=False)
    return df