from app.privacy.policy_engine import get_policy


def sanitize(text, detections, policies=None):
    """
    Replace detected PII from right to left so that
    character positions remain valid.
    """

    counters = {}
    replacements = []

    for detection in detections:
        entity_type = detection["type"]
        action = get_policy(entity_type, policies)

        counters[entity_type] = counters.get(entity_type, 0) + 1
        number = counters[entity_type]

        if action == "ANONYMIZE":
            replacement = f"[{entity_type}_{number}]"

        elif action == "MASK":
            replacement = f"[{entity_type}_MASKED]"

        elif action == "BLOCK":
            replacement = "[REDACTED]"

        else:
            continue

        replacements.append(
            (
                detection["start"],
                detection["end"],
                replacement
            )
        )

    # Remove overlapping replacements.
    # Higher-confidence detection wins.
    valid_replacements = []

    for replacement in sorted(
        replacements,
        key=lambda x: (x[0], -(x[1] - x[0]))
    ):
        start, end, _ = replacement

        overlaps = any(
            start < existing_end
            and end > existing_start
            for existing_start, existing_end, _ in valid_replacements
        )

        if not overlaps:
            valid_replacements.append(replacement)

    # Replace from right to left.
    for start, end, replacement in sorted(
        valid_replacements,
        key=lambda x: x[0],
        reverse=True
    ):
        text = text[:start] + replacement + text[end:]

    return text