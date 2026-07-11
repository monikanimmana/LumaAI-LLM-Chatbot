import chromadb #type:ignore
from .rag import read_pdf , create_chunk
from .embeddings import create_embed
from sentence_transformers import SentenceTransformer #type: ignore
client = chromadb.Client()

collection = client.get_or_create_collection(
    name="documents"
)

################## Storing Embedding in vector database ############################ 

def store_embed(chunks , embedding):

    ids = [str(i) for i in range(len(chunks))]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embedding
    )

################### return all embeddings ########################

def get_all():

    return collection.get()


################# Return the number of stored chunks.#######################

def count():

    return collection.count()


######### creating user query ##############

def semantic_search(query:str , k: int =3):

    query_embedding = model.encode(query).tolist() #type: ignore

    result = collection.query(
        query_embedding=[query_embedding],
        n_results=k
    )

    return result["documents"][0]

