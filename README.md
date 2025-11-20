# Research Summarizer
A lightweight tool for turning long research articles into clear, structured summaries.

This project takes any article URL and generates:

- A concise summary  
- Key insights  
- A simplified explanation for non-experts  
- Citations and references  
- Comprehension questions  

Built with FastAPI, Gemini, and Streamlit, it provides both a REST API and a clean web interface for quickly digesting academic content.

---

## Features

### URL-to-Summary Pipeline
Given a link to a research article (arXiv, NCBI, academic journals, long-form news, etc.), the system:

1. Extracts and cleans the article text  
2. Sends the text to an AI summarizer  
3. Produces structured JSON with summary, insights, simplified explanation, citations, and quiz questions  
4. Renders the result in a simple web UI

### Streamlit Interface
The Streamlit frontend provides a minimal, readable layout to explore:

- Summary  
- Key insights  
- Simplified explanation  
- Citations  
- Quiz questions  

### FastAPI Backend
A small FastAPI service powers the core pipeline:

- `/summarize` accepts a JSON body with `{ "url": "..." }`  
- Scrapes article content using `requests` + `BeautifulSoup`  
- Calls the AI model and returns a structured `SummaryResponse`

### AI-Powered Summaries
Uses Google’s Gemini API (e.g., `gemini-flash-latest`) to generate structured JSON output designed for programmatic consumption.

---

## Project Structure

```text
research_summarizer/
│ main.py              # FastAPI backend
│ summarizer.py        # Gemini model logic
│ scraper.py           # URL text extraction
│ models.py            # Pydantic request/response models
│ ui.py                # Streamlit interface
│ requirements.txt
│ README.md
│ .env.example
