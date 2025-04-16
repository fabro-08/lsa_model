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
    OLLAMA_MODEL = "phi4:latest"

    # configuracion ruta de logs
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # Directorio base del proyecto
    LOG_DIR = os.getenv("LOG_DIR", os.path.join(BASE_DIR, "app/logs"))

config = Config()