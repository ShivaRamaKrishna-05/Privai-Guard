from app.config import settings


async def generate(prompt: str) -> str:
    provider = settings.llm_provider.lower().strip()

    if provider in ("openai", "openrouter"):
        try:
            from langchain_openai import ChatOpenAI
            from langchain_core.messages import HumanMessage

            if not settings.llm_api_key:
                return "LLM provider is not configured. Please set the API key."

            model_kwargs = {
                "api_key": settings.llm_api_key,
                "model": settings.llm_model,
            }

            if provider == "openrouter":
                model_kwargs["base_url"] = "https://openrouter.ai/api/v1"

            model = ChatOpenAI(**model_kwargs)

            result = await model.ainvoke(
                [HumanMessage(content=prompt)]
            )

            return result.content

        except Exception:
            return (
                "LLM provider failed safely. "
                "Please verify provider configuration."
            )

    return (
        "Mock LLM response: I received your privacy-sanitized prompt. "
        "No external model was contacted."
    )