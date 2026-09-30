"""Nettoyage des textes d'avis."""
import re

import pandas as pd


def clean_text(text: str) -> str:
    """Met un avis sous une forme simple et uniforme."""
    text = str(text).lower()
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"https?://\S+|www\.\S+", " ", text)
    text = re.sub(r"\d+", " ", text)
    text = re.sub(r"[^\w\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def prepare_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """Nettoie le jeu complet : supprime vides et doublons, ajoute 'avis_propre'."""
    df = df.copy()
    df = df.dropna(subset=["avis"])
    df = df.drop_duplicates(subset="avis")
    df["avis_propre"] = df["avis"].apply(clean_text)
    df = df[df["avis_propre"].str.len() > 0]
    return df.reset_index(drop=True)