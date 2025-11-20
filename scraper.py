import requests
from bs4 import BeautifulSoup

def extract_text_from_url(url: str) -> str:
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")

    # Remove scripts, styles, navbars
    for tag in soup(["script", "style", "header", "footer", "noscript"]):
        tag.decompose()

    # Extract visible text
    paragraphs = [p.get_text(" ", strip=True) for p in soup.find_all("p")]
    text = "\n".join(paragraphs)

    return text
