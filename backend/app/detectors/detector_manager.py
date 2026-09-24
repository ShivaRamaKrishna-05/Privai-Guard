from app.detectors.regex_detector import detect as regex_detect
from app.detectors.spacy_detector import detect as spacy_detect
from app.detectors.transformer_detector import detect as transformer_detect


def _deduplicate(results):
    """
    Remove overlapping detections.

    When two detections overlap, keep the one with:
    1. Higher confidence
    2. Longer span if confidence is equal
    """

    # Highest confidence first, then longest span
    results = sorted(
        results,
        key=lambda x: (
            -x["confidence"],
            -(x["end"] - x["start"])
        )
    )

    selected = []

    for item in results:
        overlaps = any(
            item["start"] < existing["end"]
            and item["end"] > existing["start"]
            for existing in selected
        )

        if not overlaps:
            selected.append(item)

    # Return detections in their original text order
    return sorted(selected, key=lambda x: x["start"])


def detect_all(text: str):
    results = (
        regex_detect(text)
        + spacy_detect(text)
        + transformer_detect(text)
    )

    return _deduplicate(results)