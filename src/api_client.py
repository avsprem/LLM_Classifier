from openai import OpenAI
from src.config import OPENAI_API_KEY, MODEL
import time

client = OpenAI(api_key=OPENAI_API_KEY)


def get_response(prompt: str, retries: int = 3) -> str:
    for attempt in range(retries):
        try:
            response = client.responses.create(
                model=MODEL,
                input=prompt
            )
            return response.output[0].content[0].text.strip()

        except Exception as e:
            print(f"Error: {e}, retrying ({attempt+1}/{retries})...")
            time.sleep(2)

    return "ERROR"