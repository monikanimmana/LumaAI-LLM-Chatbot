# Local Chatbot

A local AI chatbot built using **FastAPI** and **Ollama (Qwen)** with real-time streaming responses.

## Features
- Local LLM using Ollama
- FastAPI REST API
- Streaming responses using Python `yield`
- Modular project structure
- JSON request/response handling

## Tech Stack
- Python
- FastAPI
- Ollama (Qwen)
- Uvicorn
- Pydantic

## Project Structure

```
local_chatbot/
├── routes/
├── services/
├── main.py
├── schemas.py
├── __init__.py
├── README.md
└── .gitignore
```

## Run the Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Start Ollama:

```bash
ollama run qwen3
```

Run the FastAPI server:

```bash
uvicorn main:app --reload
```

Open the API documentation:

```
http://127.0.0.1:8000/docs
```

## Future Improvements
- Chat history
- Multiple model support
- RAG integration
- Authentication
- Web interface