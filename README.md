# RAG-Based Customer Support Assistant

This project implements a Retrieval-Augmented Generation (RAG) system using LangGraph.

## Features
- PDF-based knowledge retrieval
- ChromaDB vector storage
- LangGraph workflow
- Conditional routing
- Human-in-the-loop (HITL)

## Tech Stack
- Python
- LangChain
- ChromaDB
- HuggingFace Embeddings

## How it works
User query → retrieve relevant chunks → generate answer → route to output or human

## Example

Q: How can customers contact support?  
A: Customers can contact support via toll-free number, email, or website.

Q: What is refund policy?  
A: Escalated to human