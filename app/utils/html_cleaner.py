from bs4 import BeautifulSoup
import re


def clean_html(html: str) -> str:

    soup = BeautifulSoup(html, "lxml")

    for tag in soup([
        "script",
        "style",
        "nav",
        "footer",
        "header",
        "noscript",
        "svg",
        "iframe",
        "aside",
        "form"
    ]):
        tag.decompose()

    text = soup.get_text(
        separator=" ",
        strip=True
    )

    text = re.sub(r"\s+", " ", text)

    return text.strip()