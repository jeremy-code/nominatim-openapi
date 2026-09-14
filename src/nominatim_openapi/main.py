from fastapi import FastAPI

from nominatim_openapi.api.main import api_router

app = FastAPI()


app.include_router(api_router)
