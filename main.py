from fastapi import FastAPI
from info import info_router
import uvicorn

app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {
        "message": "Welcome to the FastAPI application!"
    }

app.include_router(info_router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)