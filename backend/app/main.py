# app/main.py

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import health_routes, test_routes, langgraph_routes
from app.utils.logger import config_logger

logger = config_logger("main")

app = FastAPI(
    title="Traductor LSA <> SPA",
    version="0.1",
    description="Servidor API para traductor LSA <> SPA."
)

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ajustar en producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(langgraph_routes.router, prefix="/translator", tags=["translator"])
app.include_router(health_routes.router, prefix="/health", tags=["Health"])
app.include_router(test_routes.router, tags=["Test"])

# Redirect root
@app.get("/", include_in_schema=False)
async def redirect_to_docs():
    from fastapi.responses import RedirectResponse
    return RedirectResponse(url="/docs")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)