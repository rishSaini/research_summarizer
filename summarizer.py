from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

PROMPT_TEMPLATE = """
You are a research assistant. Analyze the following article text.

Return a JSON with:
- summary (5–8 bullet points)
- key_insights (3–5 bullets)
- simplified (explain the article like I'm 5)
- citations (what the model relied on)
- quiz (3 short comprehension questions)

Article text:
{{TEXT}}
"""

def summarize_text(text: str):
    prompt = PROMPT_TEMPLATE.replace("{{TEXT}}", text[:4000])  # truncate for safety

    completion = client.chat.completions.create(
        model="gpt-4.1",  
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"}
    )

    return completion.choices[0].message.content
