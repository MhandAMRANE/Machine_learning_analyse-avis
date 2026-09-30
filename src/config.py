"""Réglages centraux du projet."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
MODELS_DIR = ROOT / "models"
DATA_DIR.mkdir(exist_ok=True)
MODELS_DIR.mkdir(exist_ok=True)

MODEL_PATH = MODELS_DIR / "sentiment_model.joblib"

DATASET_NAME = "tblard/allocine"
SAMPLE_SIZE = 50_000

LABELS = {0: "Négatif", 1: "Positif"}

RANDOM_STATE = 42