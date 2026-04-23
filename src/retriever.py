def get_relevant_docs(db, query):
    return db.similarity_search(query, k=3)