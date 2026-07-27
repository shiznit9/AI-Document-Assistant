# 📄 AI Document Assistant

A modular Retrieval-Augmented Generation (RAG) application built with **LangChain**, **ChromaDB**, and **Hugging Face Embeddings**. The assistant ingests documents, creates semantic embeddings, stores them in a persistent vector database, and answers user questions using only the information contained in the uploaded documents.

Designed with a clean, modular architecture, each stage of the RAG pipeline is separated into dedicated managers, making the project easy to understand, maintain, and extend.

---

## ✨ Features

- 📄 Supports multiple document formats
  - PDF
  - DOCX
  - TXT
  - Markdown

- 🧩 Modular architecture with dedicated managers for:
  - Document Processing
  - Embeddings
  - Vector Store
  - Retrieval
  - Prompt Management
  - LLM Integration
  - RAG Pipeline

- 🔍 Semantic search using vector embeddings

- 🧠 Hugging Face embedding models

- 💾 Persistent Chroma vector database

- 📝 Automatic document metadata extraction

- 🔐 SHA-256 duplicate document detection

- 💬 Interactive command-line interface

- 📚 Source-aware responses with retrieved document chunks

- ⚙️ Centralized configuration using a settings file

---

# 🏗️ Architecture

```mermaid
flowchart TD

A[Documents] --> B[Document Loader]
B --> C[Metadata Extraction]
C --> D[Document Splitter]
D --> E[Embedding Manager]
E --> F[(Chroma Vector Store)]

User --> G[RAG Manager]

G --> H[Retriever]
H --> F
F --> I[Relevant Chunks]

I --> J[Prompt Manager]
J --> K[LLM]
K --> L[Generated Answer]
```

---

# 📂 Project Structure

```text
AI-Document-Assistant
│
├── config/
│   └── settings.py
│
├── data/
│   ├── documents/
│   └── chroma_db/
│
├── document_processing/
│   ├── document_loader.py
│   ├── document_manager.py
│   ├── document_metadata.py
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
├── ingest.py
├── run.py
├── requirements.txt
└── README.md
```

---

# ⚙️ How It Works

The application follows a standard Retrieval-Augmented Generation (RAG) workflow:

1. Documents are loaded from the data directory.
2. Metadata is extracted for every document.
3. Each document is split into smaller chunks.
4. Embeddings are generated for every chunk.
5. Embeddings are stored in a persistent Chroma vector database.
6. User queries are converted into embeddings.
7. The retriever performs semantic similarity search.
8. Retrieved context is combined with the prompt.
9. The language model generates an answer using only the retrieved context.

---

# 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/AI-Document-Assistant.git

cd AI-Document-Assistant
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment:

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ⚙️ Configuration

Update your API key inside the environment file.

```env
GOOGLE_API_KEY=your_api_key
```

Modify application settings in:

```text
config/settings.py
```

---

# 📥 Ingest Documents

Place your files inside:

```text
data/documents/
```

Then build the vector database:

```bash
python ingest.py
```

---

# 💬 Run the Assistant

```bash
python run.py
```

Example:

```text
Ask a question:
What is Retrieval-Augmented Generation?

Answer:
Retrieval-Augmented Generation (RAG) combines semantic retrieval with a language model by first retrieving relevant document chunks before generating a response.

Sources:
• ai_notes.pdf
• rag_overview.pdf
```

---

# 🛠️ Tech Stack

- Python
- LangChain
- LangChain Classic
- Google Gemini
- Hugging Face Embeddings
- ChromaDB
- Sentence Transformers

---

# 📈 Future Improvements

- Hybrid Search (Dense + BM25)
- OCR Support
- Parent-Child Retrieval
- Multi-Vector Retrieval
- LangGraph Integration
- Streaming Responses
- Conversation Memory
- Web Interface (Streamlit / React)
- Re-ranking Models
- Multi-LLM Support

---

# 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Prakhar**

If you found this project useful, consider giving it a ⭐ on GitHub.