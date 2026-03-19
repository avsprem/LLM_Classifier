from src.processor import run_pipeline
from src.config import INPUT_FILE, OUTPUT_FILE

if __name__ == "__main__":
    run_pipeline(INPUT_FILE, OUTPUT_FILE)