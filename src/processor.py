import pandas as pd
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

from src.prompts import build_prompt
from src.api_client import get_response
from src.utils import clean_output
from src.config import MAX_WORKERS


def process_row(row_text: str) -> str:
    prompt = build_prompt(row_text)
    raw_output = get_response(prompt)
    return clean_output(raw_output)


def run_pipeline(input_path: str, output_path: str):
    df = pd.read_csv(input_path)

    if "prompt" not in df.columns:
        raise ValueError("CSV must contain a 'prompt' column")

    results = []

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        results = list(
            tqdm(
                executor.map(process_row, df["prompt"]),
                total=len(df)
            )
        )

    df["prediction"] = results
    df.to_csv(output_path, index=False)

    print(f"Saved results to {output_path}")