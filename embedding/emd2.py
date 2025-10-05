from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding=OpenAIEmbeddings(model="text-embedding-3-small", dimensions=32)

doc=[
  "delhi is capital of india",
  "france is in europe",
  "germany is in europe",
]

result = embedding.embed_documents(doc)

print(str(result))