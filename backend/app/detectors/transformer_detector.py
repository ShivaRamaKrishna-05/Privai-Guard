from functools import lru_cache
from app.config import settings

@lru_cache(maxsize=1)
def get_pipeline():
    from transformers import pipeline
    return pipeline("ner", model=settings.transformer_model,
                    aggregation_strategy="simple")

def detect(text: str):
    if not settings.transformer_enabled:
        return []
    try:
        outputs = get_pipeline()(text)
        mapping = {"PER":"PERSON","ORG":"ORG","LOC":"LOC","MISC":"OTHER"}
        results = []
        for item in outputs:
            score = float(item.get("score",0))
            if score < settings.transformer_threshold:
                continue
            label = item.get("entity_group","OTHER")
            results.append({"type":mapping.get(label,label),
                            "confidence":score,
                            "start":int(item["start"]),
                            "end":int(item["end"]),
                            "source":"transformer"})
        return results
    except Exception:
        return []
