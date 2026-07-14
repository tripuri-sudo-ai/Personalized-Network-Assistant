from fastapi import FastAPI
from backend.routes import router

app = FastAPI(
    title="Personalized Networking Assistant",
    description="SmartBridge Internship Project",
    version="1.0"
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "Personalized Networking Assistant Backend Running"
    }