from app.config.research import BLOCK_PATTERNS


def is_blocked_page(text: str) -> bool:

    text = text.lower()

    for pattern in BLOCK_PATTERNS:

        if pattern in text:
            return True

    return False