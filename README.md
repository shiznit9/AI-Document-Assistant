# 📄 AI Document Assistant (RAG)

An AI-powered Document Question Answering system built using **LangChain**, **Hugging Face BGE Embeddings**, **Chroma Vector Database**, and **Mistral AI**.

The application allows users to chat with PDF documents using Retrieval-Augmented Generation (RAG).

---

## Features

- Upload any PDF document
- Automatic text extraction
- Intelligent document chunking
- Vector embeddings using **BAAI/bge-large-en-v1.5**
- Chroma Vector Database
- One Vector Database per PDF
- Semantic Search
- Question Answering using **Mistral Small**
- Modular backend architecture

---

## Tech Stack

- Python
- LangChain
- Hugging Face Embeddings
- ChromaDB
- Mistral AI
- Sentence Transformers

---

## Project Structure

```
AI-Document-Assistant/
│
├── config/
│   └── settings.py
│
├── core/
│   ├── chain.py
│   ├── embeddings.py
│   ├── llm.py
│   ├── prompt.py
│   ├── retriever.py
│   └── vector_store.py
│
├── document_processing/
│   ├── loader.py
│   └── splitter.py
│
├── services/
│   └── rag_service.py
│
├── data/
│   ├── documents/
│   └── chroma_db/
│
├── run.py
├── requirements.txt
└── README.md
```

---

## Workflow

```
PDF
   │
   ▼
PDF Loader
   │
   ▼
Text Splitter
   │
   ▼
BGE Embeddings
   │
   ▼
Chroma Vector Database
   │
   ▼
Retriever
   │
   ▼
Mistral LLM
   │
   ▼
Answer
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/AI-Document-Assistant.git
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the virtual environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
MISTRAL_API_KEY=YOUR_API_KEY
```

---

## Run the Project

## Add Documents

Place the PDF documents you want to query inside:

```text
data/documents/
```

```bash
python run.py
```

---

## Example

```
Enter PDF path:
data/documents/attention-is-all-you-need.pdf

You:
Who are the authors of this paper?

Assistant:
Ashish Vaswani
Noam Shazeer
Niki Parmar
Jakob Uszkoreit
Llion Jones
Aidan N. Gomez
Łukasz Kaiser
Illia Polosukhin
```

---

## Current Capabilities

- Semantic PDF Search
- One Chroma Database per Document
- Reuse Existing Vector Databases
- Modular Architecture
- Fast Semantic Retrieval
- Production-style Backend Design

---

## Future Improvements

- Streamlit Interface
- Multi-document Chat
- Hybrid Search (BM25 + Vector Search)
- Cross Encoder Reranker
- Source Citations
- Chat History
- Metadata Filtering
- REST API

---

## License

This project is licensed under the MIT License.