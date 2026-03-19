import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = "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"

# MODEL = "openai/gpt-5.2"   # ✅ cheaper model
# MAX_WORKERS = 5

MODEL = "gpt-5-mini"
MAX_WORKERS = 5
INPUT_FILE = "data/input.csv"
OUTPUT_FILE = "data/output.csv"
