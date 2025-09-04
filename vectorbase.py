from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from langchain_community.vectorstores import Chroma
#create embeddings
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
#sample data
texts = [
    "Vector databases enable semantic search by storing embeddings.",
    "RAG systems combine retrieval with language model generation.",
    "Embeddings capture semantic meaning in numerical form."
]

metadatas = [
    {"topic": "databases", "type": "technical"},
    {"topic": "AI", "type": "technical"},
    {"topic": "ML", "type": "technical"}
]

documents = [
    Document(page_content=text, metadata=metadatas[i])
    for i, text in enumerate(texts)
]
vectorstore = Chroma.from_documents(documents, embeddings)
#query
results = vectorstore.similarity_search_with_score("What is a RAG system?", k=2)

for doc, score in results:
    print(f"Score: {score:.3f}")
    print(f"Text: {doc.page_content}")
    print(f"Metadata: {doc.metadata}")
    print("---")