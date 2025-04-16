# app/services/llm_service.py

from typing import List

from langchain.schema import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI

from app.config import config
from app.utils.prompt_loader import load_prompts
from app.utils.logger import config_logger

logger = config_logger("llm_service")
prompts = load_prompts()

# 🔹 Instanciar el modelo de lenguaje de manera centralizada
llm = ChatOpenAI(
    model=config.LLM_MODEL,
    openai_api_key=config.API_KEY,
    openai_api_base=config.URL_OPEN_ROUTER,
    temperature=0.7
)

async def translator(prompt_user: str, sentence: str) -> str:
    try:
        print(prompt_user)
        print(sentence)
        # Armar los mensajes para LangChain
        messages = [
            SystemMessage(content=prompts['translator']['system']),
            HumanMessage(content=prompts['translator']['prompt'].format(instructions=prompt_user, text=sentence)),
        ]

        print(prompts['translator']['prompt'].format(instructions=prompt_user, text=sentence))

        # Obtener respuesta del modelo
        response = await llm.ainvoke(messages)

        return response.content

    except Exception as e:
        logger.error(f"Error en translator: {e}")
        return f"Error al traducir: {str(e)}"

