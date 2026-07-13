from fastapi import APIRouter #type:ignore
from ..schemas import ChatRequest
from ..services.llm_service import stream_llm
from fastapi.responses import StreamingResponse #type:ignore
from ..vector_store import semantic_search
from ..embeddings import create_embed

router= APIRouter()

@router.post("/chat")
def chat(req: ChatRequest):

    chunks = create_embed(req.prompt)

    content = semantic_search(chunks)

    return StreamingResponse(
        stream_llm(req.prompt , content),
        media_type="text/plain"
    )