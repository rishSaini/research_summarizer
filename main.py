from fastapi import FastAPI
from pydantic import BaseModel
from scraper import extract_text_from_url
from summarizer import summarize_text

app = FastAPI()

class URLRequest(BaseModel):
    url: str

@app.post("/summarize")
def summarize_article(req: URLRequest):
    text = extract_text_from_url(req.url)
    summary = summarize_text(text)
    return summary
