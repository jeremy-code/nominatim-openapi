from fastapi import APIRouter

from nominatim_openapi.api.routes import v1

api_router = APIRouter()
api_router.include_router(v1.router)
