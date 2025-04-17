# app/flows/graph_lsa_to_spa.py
from langgraph.graph import StateGraph
from pydantic import BaseModel
from typing import Optional, Dict, Any

from app.services.llm_service import translator
from app.utils.logger import config_logger
from app.flows.state import GraphState

logger = config_logger("translation_lsa_to_spa")

# 🔹 Nodo de traducción
async def translate_node(state: GraphState) -> GraphState:
    try:
        result = await translator(prompt_user=state.prompt_user, sentence=state.text, model=state.model)
        return state.copy(update={
            "response": {"result": result}
        })
    except Exception as e:
        logger.error(f"Error en nodo de traducción: {e}")
        return None

# 🚀 Compilación del grafo simple

def build_translation_graph():
    builder = StateGraph(GraphState)
    builder.add_node("translate", translate_node)
    builder.set_entry_point("translate")
    return builder.compile()
