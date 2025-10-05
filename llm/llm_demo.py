from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv() 


llm=OpenAI(model="gpt-4",temperature=0.9)
result = llm.invoke("Tell me a joke about programming.")

print(result)
