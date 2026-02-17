import fitz
from pathlib import Path

def extract_text_from_pdf(path: Path):
    doc = fitz.open(str(path))
    text = ""
    for page in doc:
        text += page.get_text("text") + "\n"
    doc.close()
    return text
