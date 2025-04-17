import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"))

# Cargar variables desde un archivo .env
load_dotenv()

class Config:
    # configuracion open router
    API_KEY = os.getenv("API_KEY", "default_api_key")
    #LLM_MODEL = "deepseek/deepseek-r1-distill-llama-70b:free"
    LLM_MODEL = "meta-llama/llama-3.3-70b-instruct:free"
    URL_OPEN_ROUTER = "https://openrouter.ai/api/v1"


    # configuracion ruta de logs
    API_LSA = "http://api:8000"

config = Config()