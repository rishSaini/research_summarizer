from fastapi import FastAPI
from models import URLRequest, SummaryResponse
from scraper import extract_text_from_url
from summarizer import summarize_text
import json


app = FastAPI()

@app.post("/summarize", response_model=SummaryResponse)
def summarize_article(req: URLRequest):
    text = extract_text_from_url(req.url)
    raw_output = summarize_text(text)

    # raw_output is a JSON string from the LLM, so convert it dict
    parsed = json.loads(raw_output)

    return parsed
