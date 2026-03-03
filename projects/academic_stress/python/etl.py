import pandas as pd
from pathlib import Path

# Portable path
BASE = Path(__file__).resolve().parents[1]

# Colab fallback (if needed)
# BASE = Path("/content/data-portfolio/projects/academic_stress")

RAW = BASE / "data" / "raw" / "academic_stress.csv"
OUT = BASE / "data" / "processed" / "academic_stress_clean.csv"

df = pd.read_csv(RAW)

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_", regex=False)
    .str.replace("?", "", regex=False)
)

df["timestamp"] = pd.to_datetime(
    df["timestamp"],
    format="%d/%m/%Y %H:%M:%S"
)

df["date"] = df["timestamp"].dt.strftime("%Y-%m-%d")
df["day"] = df["timestamp"].dt.day
df["month"] = df["timestamp"].dt.month
df["year"] = df["timestamp"].dt.year
df["weekday"] = df["timestamp"].dt.day_name()
df["weekyear"] = df["timestamp"].dt.isocalendar().week
df["quarter"] = df["timestamp"].dt.quarter
df["hour"] = df["timestamp"].dt.hour

df = df.drop(columns=["timestamp"])

OUT.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(OUT, index=False)

print(f"Saved to: {OUT}")
print("ETL completed successfully.")
