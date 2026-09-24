from fastapi import APIRouter, Depends

from app.schemas.chat import ChatRequest, ChatResponse
from app.auth.dependencies import current_user
from app.privacy.sanitizer import analyze_text
from app.llm.gateway import generate
from app.llm.response_scanner import scan_response
from app.database.mongodb import events_collection
from app.database.models import event_document

router = APIRouter(tags=["Chat"])


@router.post("/chat", response_model=ChatResponse)
async def chat(data: ChatRequest, user=Depends(current_user)):

    # 1. Analyze the user's original prompt
    analysis = analyze_text(data.prompt)

    # 2. Block or process the prompt
    if analysis["action"] == "BLOCK":

        response = (
            "[Request blocked because it contained "
            "prohibited sensitive information.]"
        )

        response_detections = []
        response_action = "BLOCK"

    else:

        # 3. Send the sanitized prompt to the LLM
        response = await generate(analysis["sanitized_text"])

        # 4. Scan the generated response for sensitive information
        response_detections, response_action, response = scan_response(response)

    # 5. Record the chat event
    await events_collection.insert_one(
        event_document(
            user["sub"],
            "chat-request",
            analysis["detections"],
            analysis["risk_score"],
            analysis["risk_level"],
            analysis["action"]
        )
    )

    # 6. Return the result to the frontend
    return {
        "original_prompt": data.prompt,
        "sanitized_prompt": analysis["sanitized_text"],
        "prompt_detections": analysis["detections"],
        "response": response,
        "response_detections": response_detections,
        "response_action": response_action,
        "risk_score": analysis["risk_score"],
        "risk_level": analysis["risk_level"]
    }