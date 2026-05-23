# Local Agentic RAG Pipeline

A fully local, privacy-first Multi-Agent Retrieval-Augmented Generation (RAG) pipeline built for secure document analysis, compliance validation, and hallucination-resistant AI workflows.

---

## Project Overview

This project is a production-oriented local RAG architecture designed to process sensitive business documents completely offline without relying on external cloud APIs.

The system combines:

- Local vector storage
- Semantic retrieval
- Multi-agent orchestration
- Compliance verification
- Offline LLM inference using Ollama

The pipeline separates responsibilities across specialized AI agents to improve factual reliability and reduce hallucinations.

---

## Core Features

- Fully offline execution
- Privacy-focused document processing
- Multi-agent architecture
- Retrieval-Augmented Generation (RAG)
- Compliance verification layer
- Local vector database storage
- Semantic similarity search
- Markdown-based cited outputs
- Lightweight orchestration design
- CPU/GPU compatible deployment

---

#  System Architecture

## Architecture Type

**Edge Inference / Multi-Agent Retrieval-Augmented Generation**

---

## Pipeline Layers

| Layer | Component | Technology | Purpose |
|---|---|---|---|
| Storage & Retrieval | Persistent Vector Store | ChromaDB + all-MiniLM-L6-v2 | Converts documents into embeddings for semantic retrieval |
| Extraction Layer | Research Analyst Agent | Ollama + Local LLM | Extracts relevant factual information |
| Compliance Layer | Compliance Officer Agent | Ollama + Verification Prompting | Verifies extracted data against source context |

---

# Operational Workflow

1. User submits a query through the terminal interface.
2. Query is embedded using `all-MiniLM-L6-v2`.
3. Semantic similarity search is executed against the local vector database.
4. Matching document chunks are retrieved with metadata.
5. Context is sent to the **Research Analyst Agent**.
6. Initial factual response is generated.
7. Draft response and raw source text are forwarded to the **Compliance Officer Agent**.
8. Final verified Markdown response is returned with citations.

---

# Technology Stack

## AI & NLP

- Ollama
- Llama 3.2
- Sentence Transformers
- LangChain Community Utilities

## Storage & Retrieval

- ChromaDB
- Persistent Vector Database

## Programming Language

- Python 3.10 – 3.11

---

# Project Structure

```bash
local-agentic-rag-pipeline/
│
├── app.py
├── requirements.txt
├── local_vector_db/
├── 
└── README.md
```

---

# Installation Guide

## 1. Install Ollama

Download and install Ollama from:

https://ollama.com

---

## 2. Pull the Local Model

```bash
ollama run llama3.2
```

---

## 3. Clone Repository

```bash
git clone https://github.com/sindhudb/local-agentic-rag-pipeline.git
cd local-agentic-rag-pipeline
```

---

## 4. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 6. Run Application

```bash
python app.py
```

---

# Interactive Usage

Example query:

```text
What is the refund policy mentioned in the compliance document?
```

Exit commands:

```text
exit
quit
```

---

# Key Dependencies

```txt
huggingface-hub>=0.34.0
sentence-transformers==2.6.1
chromadb==0.4.15
langchain-community>=0.0.20
```

---

# Engineering Challenges & Solutions

## Problem

Traditional multi-agent frameworks introduced dependency conflicts and compilation failures due to native build requirements such as:

- `tiktoken`
- `regex`
- Visual Studio C++ compiler dependencies

These caused installation instability on systems lacking full build toolchains.

---

## Solution

The pipeline was redesigned using:

- Lightweight native orchestration
- Minimal dependency layers
- Stable precompiled Python packages
- Simplified LangChain integrations

This significantly improved portability and deployment reliability.

---

# Terminal Noise Suppression

Older ChromaDB implementations generated verbose telemetry warnings during retrieval operations.

To maintain a clean enterprise-grade terminal interface, stderr redirection was implemented:

```python
sys.stderr = open(os.devnull, 'w')
```

This suppresses unnecessary background warnings during execution.

---

# Privacy & Security Advantages

Unlike cloud-hosted AI systems, this architecture:

- Keeps sensitive documents local
- Eliminates external API exposure
- Prevents proprietary data leakage
- Enables secure enterprise deployment
- Supports offline environments

---

# Why This Project Matters

This project demonstrates:

- Real-world AI systems engineering
- Production-grade RAG design
- Multi-agent orchestration
- Local LLM deployment
- Secure AI infrastructure
- Compliance-aware AI pipelines

It is designed as more than a tutorial implementation — it represents a scalable engineering-focused local AI architecture.

---

# Repository

GitHub Repository:

https://github.com/sindhudb/local-agentic-rag-pipeline

---

---

# Author

Developed by Sindhu D B

Focused on:
- Artificial Intelligence
- Full Stack Development
- Local AI Systems
- Secure Enterprise AI Pipelines

