import ollama #type:ignore
from ..vector_store import semantic_search

chat_history=[
    {
        "role":"System",
        "content":"You are a helpful AI assistant."
        "Answer ONLY using the provided context. "
        "If the answer is not present, say you don't know."
    }
]

def stream_llm(question:str,content:str):

    messages=chat_history.copy()

    messages.append(
        {
            "role":"user",
            "content": f"""

            "context":{content},
            "question":{question},

            answer=
            """
        }
    )
    

    stream = ollama.chat(
        model="qwen3",
        messages=messages,
        stream=True
    )

    answer=""

    for chunk in stream:
        text=chunk["message"]["content"]
        answer+=text
        yield text

 # Store only the conversation, not the retrieved context
    chat_history.append(
        {
            "role":"user",
            "content":question
        }
    )

    chat_history.append(
        {
            "role":"assistant",
            "content":answer
        }
    )

def chat(question: str):
    chunks = semantic_search(question)
    context = "\n\n".join(chunks)
    return stream_llm(question, context)

   