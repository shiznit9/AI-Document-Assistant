# AI Document Assistant

An AI-powered Document Assistant built with **LangChain**, **ChromaDB**, **Hugging Face Embeddings**, and **Mistral AI**.

The application allows users to ingest documents, generate vector embeddings, store them in a persistent vector database, and ask natural language questions using Retrieval-Augmented Generation (RAG).

---

## Features

- Support for multiple document formats
  - PDF
  - DOCX
  - TXT
  - Markdown
  - HTML
  - CSV
  - Excel
  - PowerPoint
  - JSON
  - XML
  - Email (.eml)

- Automatic document chunking
- Hugging Face sentence embeddings
- Persistent Chroma vector database
- Semantic similarity search
- Retrieval-Augmented Generation (RAG)
- Modular architecture following separation of concerns
- CLI-based chat interface

---

## Project Structure

```
AI-DOCUMENT-ASSISTANT/
│
├── config/
│   └── settings.py
│
├── data/
│   ├── chroma_db/
│   └── documents/
│
├── document_processing/
│   ├── document_loader.py
│   ├── document_manager.py
│   └── document_splitter.py
│
├── embeddings/
│   └── embedding_manager.py
│
├── llm/
│   └── llm_manager.py
│
├── prompts/
│   └── prompt_manager.py
│
├── rag/
│   └── rag_manager.py
│
├── retrieval/
│   └── retriever_manager.py
│
├── vector_store/
│   └── vector_store_manager.py
│
├── requirements/
│
├── run.py
├── README.md
└── .gitignore
```

---

## Architecture

```
                Documents
                    │
                    ▼
            Document Loader
                    │
                    ▼
           Document Splitter
                    │
                    ▼
         Embedding Generator
                    │
                    ▼
           Chroma Vector Store
                    │
                    ▼
               Retriever
                    │
                    ▼
             Prompt Template
                    │
                    ▼
               Mistral LLM
                    │
                    ▼
                  Answer
```

---

## Tech Stack

- Python
- LangChain
- ChromaDB
- Hugging Face Embeddings
- Mistral AI
- Sentence Transformers

---

## Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/AI-document-assistant.git

cd AI-document-assistant
```

---

### Create a virtual environment

Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

### Install dependencies

```bash
pip install -r requirements/requirements.txt
```

If you want support for additional document loaders:

```bash
pip install -r requirements/requirements-loaders.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

Example:

```env
MISTRAL_API_KEY=your_api_key_here
```

---

## Usage

### Step 1

Place your documents inside

```
data/documents/
```

---

### Step 2

Ingest the documents using the document manager.

(Your ingestion script or future UI will handle this.)

---

### Step 3

Run the application

```bash
python run.py
```

Example

```
Ask a question:

> What is the marking scheme?

Answer:

The marking scheme is...
```

---

## Supported Document Types

| Format | Supported |
|---------|-----------|
| PDF | ✅ |
| DOCX | ✅ |
| TXT | ✅ |
| Markdown | ✅ |
| HTML | ✅ |
| CSV | ✅ |
| Excel | ✅ |
| PowerPoint | ✅ |
| JSON | ✅ |
| XML | ✅ |
| Email (.eml) | ✅ |

---

## Current Features

- Document ingestion
- Automatic text chunking
- Hugging Face embeddings
- Persistent Chroma database
- Semantic retrieval
- RAG pipeline
- Interactive CLI

---

## Planned Features

- Document metadata support
- Source citations
- Page references
- Multi-document filtering
- Delete/update individual documents
- Streamlit web interface
- Conversation memory
- Hybrid Search (BM25 + Vector Search)
- Reranking
- Docker support
- FastAPI REST API

---

## License

This project is for educational and portfolio purposes.