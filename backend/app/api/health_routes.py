# app/api/health_routes.py

from fastapi import APIRouter, Depends
#from sqlalchemy.ext.asyncio import AsyncSession
#from app.db.connection import get_db
#from app.db.health_check import check_database_connection

router = APIRouter()

# @router.get("/db")
# async def health_db(db: AsyncSession = Depends(get_db)):
#     return await check_database_connection(db)

@router.get("/status")
def status():
    return {"status": "running"}