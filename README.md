# Proyecto: Traductor LSA ⬌️ SPA

Este proyecto implementa un traductor automático entre Lengua de Señas Argentina (LSA) y Español, utilizando modelos de lenguaje grandes (LLMs) a través de LangChain, FastAPI y Streamlit.

![Interfaz del Traductor LSA ⬌️ SPA](./img/UI.jpg)

## Instalación de Docker

### Windows
1. Descargar e instalar Docker Desktop desde [Docker Desktop for Windows](https://www.docker.com/products/docker-desktop/).
2. Habilitar WSL 2 y reiniciar la PC si es necesario.

### Mac
1. Descargar e instalar Docker Desktop desde [Docker Desktop for Mac](https://www.docker.com/products/docker-desktop/).
2. Seguir las instrucciones del instalador.

### Linux
```bash
# Instalación rápida para distribuciones basadas en Debian/Ubuntu:
sudo apt update
sudo apt install docker.io docker-compose-plugin

# Habilitar Docker
sudo systemctl start docker
sudo systemctl enable docker
```

Verificar instalación:
```bash
docker --version
docker compose version
```


## Ejecución del proyecto

1. Clonar el repositorio.
2. Crear un archivo `.env` en las carpetas `backend/env` y `frontend/env`.
3. Dentro de cada `.env` definir la variable:

```bash
API_KEY=tu_api_key_aqui
```

> Nota: La API_KEY debe ser obtenida desde [openrouter.ai](https://openrouter.ai/) y es utilizada para autenticar el acceso a los modelos de lenguaje (LLMs) que permiten realizar las traducciones.

4. Ejecutar el proyecto con Docker Compose:

```bash
docker compose up --build
```

Esto levantará los servicios de backend (FastAPI) y frontend (Streamlit) automáticamente.


## Estructura del proyecto

```
.
├── backend
│   ├── app
│   │   ├── api           # Rutas de la API (FastAPI)
│   │   ├── db            # Lógica relacionada a base de datos (en progreso)
│   │   ├── flows         # Flujos de procesamiento de traducción LangGraph
│   │   ├── logs          # Logs de la aplicación
│   │   ├── main.py       # Punto de entrada FastAPI
│   │   ├── models        # Modelos de datos (en progreso)
│   │   ├── services      # Servicios de negocio (ej. invocación a LLM)
│   │   └── utils         # Utilidades como logger y carga de prompts
│   ├── dockerfile        # Dockerfile del backend
│   └── env               # Configuraciones y dependencias
├── docker-compose.yaml   # Orquestador de servicios Docker
├── frontend
│   ├── app
│   │   ├── config.py     # Configuraciones frontend
│   │   ├── env           # Configuraciones y dependencias
│   │   └── main.py       # Aplicación Streamlit
│   ├── dockerfile        # Dockerfile del frontend
├── lab
│   ├── notebooks         # Experimentación y desarrollo (Jupyter Notebooks)
```

**Nota:** Los archivos `.pyc` y `.env` no forman parte relevante de la estructura.


## Variables de entorno

Cada carpeta `env/` debe contener un archivo `.env` con la siguiente variable:

```bash
API_KEY=tu_api_key_de_modelo
```

> La `API_KEY` debe ser obtenida desde [openrouter.ai](https://openrouter.ai/), una plataforma que facilita el acceso a diversos modelos de lenguaje (LLMs) como GPT-4, Claude, entre otros.

Esta clave se usa para autenticar llamadas a la API del modelo de lenguaje.


## Tecnologías utilizadas

- **Frontend:** desarrollado con **Streamlit**, para interfaz rápida de carga de textos y visualización de resultados.
- **Backend:** construido con **FastAPI** para exponer servicios HTTP, integrando flujos de procesamiento de prompts mediante **LangChain** y **LangGraph**.

---

✨ Proyecto orientado a facilitar la traducción entre lenguaje de señas argentino (LSA) y español usando IA generativa.