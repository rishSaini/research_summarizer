import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("GEMINI_API_KEY not set in .env")

genai.configure(api_key=api_key)

PROMPT_TEMPLATE = """
You are a research assistant. Analyze the following article text.

Return a JSON object with keys:
- summary: 5–8 bullet points
- key_insights: 3–5 bullet points
- simplified: explaining the article like I'm 5
- citations: a list of references the model relied on
- quiz: 3 short comprehension questions

Article text:
{{TEXT}}

IMPORTANT:
Return ONLY valid JSON. No backticks. No markdown. No explanation.
"""

def summarize_text(text: str) -> str:
    prompt = PROMPT_TEMPLATE.replace("{{TEXT}}", text[:6000])

    model = genai.GenerativeModel("gemini-flash-latest")  

    result = model.generate_content(
        prompt,
        generation_config={
            "response_mime_type": "application/json"
        }
    )

    # Gemini returns a text string that should already be JSON
    return result.text
