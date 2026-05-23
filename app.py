import os
import sys

# CRITICAL FIX: Intercept and hide ChromaDB's telemetry print errors completely
sys.stderr = open(os.devnull, 'w')

from langchain_community.llms import Ollama
from langchain_community.embeddings import HuggingFaceEmbeddings
import chromadb

print("====================================================")
print("     LOCAL MULTI-AGENT RAG PRODUCTION ENTERPRISE     ")
print("====================================================")

print("\n1. Hooking into Local Inference Infrastructure...")
# Connecting to your successfully downloaded llama3.2 engine
local_llm = Ollama(model="llama3.2") 

# Initializing a lightweight embedding transformer running entirely on your local processor
embedding_function = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

print("2. Constructing Local Vector Store Database...")
# Creating a persistent client to save your vector chunks directly onto your disk
chroma_client = chromadb.PersistentClient(path="./local_vector_db")
collection = chroma_client.get_or_create_collection(name="corporate_docs")

# Sample mock documents matching corporate requirements
mock_docs = [
    {"id": "doc1", "text": "Refund Policy: Customers can request a full refund within 30 days of purchase by contacting support@company.com.", "source": "policy_manual.pdf"},
    {"id": "doc2", "text": "Security Protocol: Dual-factor authentication (2FA) is mandatory for all internal employee dashboard access loops.", "source": "security_guide.docx"}
]

if collection.count() == 0:
    print("-> Seeding context blocks into the local vector database...")
    for doc in mock_docs:
        vector = embedding_function.embed_query(doc["text"])
        collection.add(
            ids=[doc["id"]],
            embeddings=[vector],
            documents=[doc["text"]],
            metadatas=[{"source": doc["source"]}]
        )

def search_local_vault(query: str) -> str:
    """Queries the local ChromaDB index for matching content segments."""
    query_vector = embedding_function.embed_query(query)
    results = collection.query(query_embeddings=[query_vector], n_results=1)
    
    if results and 'documents' in results and results['documents']:
        matched_text = results['documents'][0][0]
        source_file = results['metadatas'][0][0]['source']
        return f"Context found in [{source_file}]: {matched_text}"
    return "No matching internal source documents found."

# ==========================================
#     CORE APPLICATION EXECUTION LOOP
# ==========================================
print("\n>>> System Boot Complete. Application Is Online.")
print(">>> (Type 'exit' or 'quit' at any prompt to terminate the session)\n")

while True:
    print("-" * 60)
    user_question = input("Enter your compliance or document inquiry: ").strip()
    
    # Check for application termination command
    if user_question.lower() in ['exit', 'quit', '']:
        print("\nShutting down local agent channels. Goodbye.")
        break
        
    print("\n[System] Pulling context matching query boundaries...")
    retrieved_context = search_local_vault(user_question)
    print(f"[System] Database Retrieval Complete.")

    # Agent 1: Senior Document Research Analyst Loop
    print("\n--- Running: Senior Document Research Analyst ---")
    analyst_prompt = f"""
    You are a Senior Document Research Analyst. Your goal is to extract data from the internal storage vault to address queries.
    You are an expert at navigating documentation databases and isolating technical data blocks.

    Analyze this raw retrieved database context: '{retrieved_context}' 
    To fulfill this question: '{user_question}'

    Provide a structured summary highlighting the key answer data and naming the exact file source.
    """
    analyst_output = local_llm.invoke(analyst_prompt)
    print(f"Analyst Output Complete.")

    # Agent 2: Compliance and Verification Officer Loop
    print("--- Running: Compliance and Verification Officer ---")
    verification_prompt = f"""
    You are a Compliance and Verification Officer. Your goal is to verify that findings are entirely accurate and do not introduce outside assumptions.
    You protect against AI hallucinations. If data is missing from the source context, you call it out.

    Review this summary compiled by the analyst: '{analyst_output}'
    Cross-verify it with the original raw database context: '{retrieved_context}'

    Ensure it adds no assumptions or outside data. Provide a clean, verified final response in Markdown format containing explicit source file mentions.
    """
    final_output = local_llm.invoke(verification_prompt)

    print("\n=== SYSTEM FINAL OUTPUT ===")
    print(final_output)
    print("\n")  # Generates spacing before next loop iteration