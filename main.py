from fastapi import FastAPI
from models import URLRequest, SummaryResponse
from scraper import extract_text_from_url
from summarizer import summarize_text
from fastapi import HTTPException
import json


app = FastAPI()

@app.post("/summarize", response_model=SummaryResponse)
def summarize_article(req: URLRequest):
    text = extract_text_from_url(req.url)
    raw_output = summarize_text(text)

    try:
        parsed = json.loads(raw_output)
    except json.JSONDecodeError:
        print("Model returned non-JSON:", raw_output)
        raise HTTPException(status_code=502, detail="Model returned invalid JSON")

    return parsed
