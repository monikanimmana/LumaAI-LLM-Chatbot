from fastapi import FastAPI  ,UploadFile , File   #type:ignore
from local_chatbot.env.routes.chat import router #type:ignore
import os
import shutil
from .rag import index_pdf


app=FastAPI()

app.include_router(router)

@app.post('upload/')
async def upload_pdf(file:UploadFile = File(...)):
    os.makedirs("app/documents",exist_ok=True)
    file_path=f"app/documents/{file.filename}"

    with open(file_path,"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)

    index_pdf(file_path)

    return {"message": "PDF indexed successfully"}

