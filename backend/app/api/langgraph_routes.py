from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.flows.graph_lsa_to_spa import build_translation_graph

router = APIRouter()

class TranslationInput(BaseModel):
    text: str
    prompt_user: str
    model: str = "microsoft/phi-4"  # Default model

@router.post("/translator_lsa")
async def translate_to_lsa(payload: TranslationInput):
    try:
        graph = build_translation_graph()
        initial_state = {
            "text": payload.text,
            "prompt_user": payload.prompt_user,
            "model": payload.model,
        }
        result = await graph.ainvoke(initial_state)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en traducción LSA: {str(e)}")

# {
#   "text": "El precio de la compu es alto",
#   "prompt_user": "- LSA significa lengua de señas argentina. Es un sistema de comunicación que se utiliza en Argentina.\n- La oración en LSA tiene la siguiente estructura: tiempo + sujeto + objeto + verbo(infinitivo) + circunstanciales\n- En LSA los artículos no se señan y tampoco existe el verbo ser por ejemplo... la oración 'Juan es alto, delgado y bueno', las señas serían 'Juan alto, delgado, bueno'\n- Cuando el verbo 'estar' está a continuación de un adjetivo se quita de la oración.\n\nEjemplos:\n'yo comí una manzana ayer' en LSA se traduce a 'ayer yo manzana comer'\n'hoy tenemos evaluación de matemática' en LSA se traduce 'hoy evaluación matemática hay'\n'Juan viene en auto' en LSA se traduce 'Juan auto venir'"
# } 


@router.post("/translator_spa")
async def translate_to_spa(payload: TranslationInput):
    try:
        graph = build_translation_graph()
        initial_state = {
            "text": payload.text,
            "prompt_user": payload.prompt_user,
            "model": payload.model,
        }
        result = await graph.ainvoke(initial_state)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en traducción LSA: {str(e)}")
    
# {
#   "text": "precio compu alto",
#   "prompt_user": "- LSA significa lengua de señas argentina. Es un sistema de comunicación que se utiliza en Argentina.\n- La oración en LSA tiene la siguiente estructura: tiempo + sujeto + objeto + verbo(infinitivo) + circunstanciales\n- En LSA los artículos no se señan y tampoco existe el verbo ser por ejemplo... la oración \"Juan es alto, delgado y bueno\", las señas serían \"Juan alto, delgado, bueno\"\n\nEjemplos:\n\"yo comí una manzana ayer\" en LSA se traduce a \"ayer yo manzana comer\".\n\"hoy tenemos evaluación de matemática\" en LSA se traduce \"hoy evaluación matemática hay\"\n\"Juan viene en auto\" en LSA se traduce \"Juan auto venir\""
# }