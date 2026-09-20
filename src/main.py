# import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI
from .db import engine
from .models import Base

@asynccontextmanager
async def lifespan(app:FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose()


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello world!"}
# app.include_router(router)

# if __name__ == "__main__":
#     uvicorn.run("main:app", reload = True)