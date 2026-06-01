import tiktoken
import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
client = OpenAI()

def analyze_sentence(sentence):
    print(f"Analyzing sentence: {sentence}")

    enc = tiktoken.encoding_for_model("gpt-4")
    tokens = enc.encode(sentence)

    print(f"Original sentence: {sentence}")
    print(f"Tokens: {tokens}")
    print(f"Number of tokens: {len(tokens)}")

    embeddings = []
    resp = client.embeddings.create(
        model="text-embedding-3-small",
        input=sentence
    )
    embedding = resp.data[0].embedding
    print(f"Embedding length: {len(embedding)}")

analyze_sentence("Agentic AI agents can plan, reason, and use tools.")

print("\n")