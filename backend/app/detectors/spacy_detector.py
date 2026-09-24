def detect(text: str):
    try:
        import spacy
        try:
            nlp = spacy.load("en_core_web_sm")
        except Exception:
            return []
        doc = nlp(text)
        allowed = {"PERSON","ORG","GPE","LOC","DATE"}
        return [{"type":ent.label_,"confidence":0.80,
                 "start":ent.start_char,"end":ent.end_char,"source":"spacy"}
                for ent in doc.ents if ent.label_ in allowed]
    except Exception:
        return []
