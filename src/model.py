from langchain.chat_models import init_chat_model
from config.settings import (
    OPENAI_API_KEY,
    OPENAI_BASE_URL,
    MODEL_NAME,
)

model = init_chat_model(
    model=MODEL_NAME,
    model_provider="openai",
    openai_api_key=OPENAI_API_KEY,
    base_url=OPENAI_BASE_URL,
)