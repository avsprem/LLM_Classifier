def build_prompt(row_text: str) -> str:
    return f"""
You are a classification model.

Given the following person details, predict whether their salary is greater than 50,000 USD.

Rules:
- Output only YES or NO
- Do not explain

Input:
{row_text}
"""