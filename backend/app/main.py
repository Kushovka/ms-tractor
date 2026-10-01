from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.staticfiles import StaticFiles

from app.api.events import router as events_router
from app.api.leads import router as leads_router
from app.api.equipment import router as equipment_router
from app.core.config import settings


app = FastAPI(title="M & S Tractor & Equipment API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(GZipMiddleware, minimum_size=1000)


@app.middleware("http")
async def add_media_cache_headers(request, call_next):
    response = await call_next(request)
    if request.url.path.startswith("/media/"):
        response.headers["Cache-Control"] = "public, max-age=31536000, immutable"
        if request.url.path.endswith(".webp"):
            response.headers["Content-Type"] = "image/webp"
    return response

app.include_router(leads_router)
app.include_router(equipment_router)
app.include_router(events_router)
app.mount("/media", StaticFiles(directory="app/static/media"), name="media")


@app.get("/health")
def health_check():
    return {"status": "ok"}
