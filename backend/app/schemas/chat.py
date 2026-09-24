from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    prompt: str = Field(min_length=1, max_length=12000)


class ChatResponse(BaseModel):
    original_prompt: str
    sanitized_prompt: str
    prompt_detections: list[dict]
    response: str
    response_detections: list[dict]
    response_action: str
    risk_score: int
    risk_level: str