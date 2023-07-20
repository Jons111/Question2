import urllib.parse
from fastapi import FastAPI
app = FastAPI(
    title="Question2",)

def encode_link(link):
    """Encode a link."""
    return urllib.parse.quote_plus(link)


@app.get("/encode_link")
def encode_link_endpoint(link: str) -> str:
    """Encode a link."""
    encoded_link = encode_link(link)
    return encoded_link