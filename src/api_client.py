from openai import OpenAI
from src.config import OPENAI_API_KEY, MODEL
import time

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENAI_API_KEY,
)

def get_response(prompt: str, retries: int = 3) -> str:
    for attempt in range(retries):
        try:
            # Only use max_output_tokens for OpenRouter
            response = client.chat.completions.create(
                model=MODEL,
                max_tokens=25,  
                messages=[
                    {"role": "system", "content": "Answer only YES or NO."},
                    {"role": "user", "content": prompt},
                ],
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"Error: {e}, retrying ({attempt+1}/{retries})...")
            time.sleep(2)
    return "ERROR"
