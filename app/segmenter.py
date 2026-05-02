"""
Splits text into alternating Nepali (Devanagari) and non-Nepali segments,
so only Nepali unicode is sent to the converter.
"""

import re

# Devanagari unicode block: U+0900–U+097F
# Also include the Devanagari Extended block U+A8E0–U+A8FF and
# common combining marks that travel with Devanagari glyphs.
NEPALI_PATTERN = re.compile(r"([\u0900-\u097F\u0951-\u0952\u0964-\u0965]+)")


def segment_text(text: str) -> list[tuple[str, bool]]:
    """
    Split *text* into a list of (chunk, is_nepali) tuples preserving order.

    Example:
        "Hello नमस्ते World"
        → [("Hello ", False), ("नमस्ते", True), (" World", False)]
    """
    parts = NEPALI_PATTERN.split(text)
    segments = []
    for i, part in enumerate(parts):
        if not part:  # skip empty strings produced by split()
            continue
        is_nepali = bool(NEPALI_PATTERN.fullmatch(part))
        segments.append((part, is_nepali))
    return segments
