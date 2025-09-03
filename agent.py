from langchain_groq import ChatGroq

llm = ChatGroq(model="llama-3.1-8b-instant")
response = llm.invoke("Write a haiku about AI agents.")
print(response)