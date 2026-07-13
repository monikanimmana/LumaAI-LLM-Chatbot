import chromadb #type:ignore
from .rag import read_pdf , create_chunk
from .embeddings import create_embed

client = chromadb.Client()

collection = client.get_or_create_collection(
    name="documents"
)

def semantic_search(query:str , k: int =3):

    query_embedding = create_embed(query).tolist() #type: ignore

    result = collection.query(
        query_embeddings=[query_embedding],
        n_results=k
    )

    return result["documents"][0]

