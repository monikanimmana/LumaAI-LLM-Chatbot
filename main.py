from fastapi import FastAPI
from routes.chat import router

app=FastAPI()

app.include_router(router)