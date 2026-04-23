from loader import load_pdf
from chunking import chunk_data
from embedding import create_vector_store
from retriever import get_relevant_docs
from graph import graph

docs = load_pdf("data/support.pdf")
chunks = chunk_data(docs)
db = create_vector_store(chunks)

while True:
    query = input("Ask: ")

    print("\n🔍 Retrieving from knowledge base...\n")

    docs = get_relevant_docs(db, query)

    result = graph.invoke({
        "query": query,
        "docs": docs
    })

    print(result["answer"])