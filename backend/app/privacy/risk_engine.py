DEFAULT_WEIGHTS = {
    "PERSON":15,"ORG":10,"GPE":10,"LOC":15,"DATE":10,
    "EMAIL":35,"PHONE":35,"IP_ADDRESS":25,"URL":10,"ADDRESS":55,
    "CREDIT_CARD":85,"FINANCIAL":90,"GOVERNMENT_ID":90,
    "ACCOUNT_NUMBER":70,"CREDENTIAL":100,"OTHER":20,
}

def calculate_risk(detections, text=""):
    score = min(100, sum(DEFAULT_WEIGHTS.get(d["type"],20) for d in detections))
    types = {d["type"] for d in detections}
    if "PERSON" in types and types & {"EMAIL","PHONE","ADDRESS","FINANCIAL","GOVERNMENT_ID"}:
        score = min(100, score+15)
    if score <= 25: level="LOW"
    elif score <= 50: level="MEDIUM"
    elif score <= 75: level="HIGH"
    else: level="CRITICAL"
    return score, level
