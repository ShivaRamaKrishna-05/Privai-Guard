DEFAULT_POLICIES = {
    "PERSON":"ANONYMIZE","ORG":"ALLOW","GPE":"ALLOW","LOC":"ANONYMIZE",
    "DATE":"ALLOW","EMAIL":"ANONYMIZE","PHONE":"MASK","IP_ADDRESS":"MASK",
    "URL":"ALLOW","ADDRESS":"ANONYMIZE","CREDIT_CARD":"BLOCK",
    "FINANCIAL":"BLOCK","GOVERNMENT_ID":"BLOCK","ACCOUNT_NUMBER":"MASK",
    "CREDENTIAL":"BLOCK","OTHER":"WARN",
}

def get_policy(entity_type, policies=None):
    return (policies or DEFAULT_POLICIES).get(entity_type,"WARN")

def aggregate_action(detections, policies=None):
    actions=[get_policy(d["type"],policies) for d in detections]
    priority={"BLOCK":5,"ANONYMIZE":4,"MASK":3,"WARN":2,"ALLOW":1}
    return max(actions,key=lambda x:priority[x]) if actions else "ALLOW"
