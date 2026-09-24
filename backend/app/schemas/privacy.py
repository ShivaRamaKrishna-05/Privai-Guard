from pydantic import BaseModel, Field

class AnalyzeRequest(BaseModel):
    text: str = Field(min_length=1, max_length=12000)

class Detection(BaseModel):
    type: str
    confidence: float
    start: int
    end: int
    source: str

class AnalysisResponse(BaseModel):
    detections: list[Detection]
    risk_score: int
    risk_level: str
    action: str
    sanitized_text: str
    detection_sources: list[str]
