import chromadb #type:ignore
from .rag import read_pdf , create_chunk
from .embeddings import create_embed

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

