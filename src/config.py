import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

MODEL = "gpt-5-mini"
MAX_WORKERS = 5
INPUT_FILE = "data/input.csv"
OUTPUT_FILE = "data/output.csv"