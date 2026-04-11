from pathlib import Path
import pandas as pd

def load_ml1m_ratings(raw_dir: str | Path) -> pd.DataFrame:
    path = Path(raw_dir) / "ratings.dat"
    df = pd.read_csv(
        path, sep="::", engine="python", header=None,
        names=["user_id", "item_id", "rating", "timestamp"],
        dtype={"user_id": "int32", "item_id": "int32", "rating": "int8", "timestamp": "int64"},
    )
    return df

def load_ml1m_movies(raw_dir: str | Path) -> pd.DataFrame:
    path = Path(raw_dir) / "movies.dat"
    df = pd.read_csv(
        path, sep="::", engine="python", header=None, encoding="latin-1",
        names=["item_id", "title", "genres"],
        dtype={"item_id": "int32"},
    )
    return df

def load_tmdb_metadata(raw_dir: str | Path) -> pd.DataFrame:
    path = Path(raw_dir) / "movies_metadata.csv"
    df = pd.read_csv(path, low_memory=False)
    keep = ["id", "imdb_id", "title", "overview", "genres", "keywords", "popularity"]
    keep = [c for c in keep if c in df.columns]
    return df[keep]
