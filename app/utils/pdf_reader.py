import fitz


def extract_pdf_text(pdf_bytes: bytes) -> str:

    text_parts = []

    pdf = fitz.open(
        stream=pdf_bytes,
        filetype="pdf"
    )

    for page in pdf:

        try:
            text_parts.append(
                page.get_text()
            )

        except Exception:
            continue

    return "\n".join(text_parts)