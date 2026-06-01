import os

from langchain.docstore.document import Document
from langchain.chains import RetrievalQA

#from langchain.vectorstores import FAISS
#from langchain.embeddings.openai import OpenAIEmbeddings
#from langchain.chat_models import ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI

from dotenv import load_dotenv
load_dotenv()


kb = [
    "Agentic AI agents use memory, tools, and goals to act.",
    "LangChain and CrewAI are popular frameworks for building AI agents.",
    "Retrieval-Augmented Generation (RAG) improves accuracy by fetching external knowledge."
]
questions = [
    "What are the key components of Agentic AI?",
    "Name one framework for AI agents.",
    "How does RAG improve answers?"
]


# Build vector DB
docs = [Document(page_content=x) for x in kb]

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

db = FAISS.from_documents(docs, embeddings)
 
retriever = db.as_retriever()

qa = RetrievalQA.from_chain_type(
    llm = ChatOpenAI(model="gpt-4o-mini"),
    retriever=retriever
)

for q in questions:
    result = qa.invoke({"query": q})

    print("\nQ:", q)
    print("A:", result["result"])
