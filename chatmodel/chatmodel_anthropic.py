from langchain import chatantropic
from dotenv import load_dotenv  

load_dotenv()

model=chatantropic.ChatAnthropic(model="claude-2", temperature=0.9)

result = model.invoke("Tell me a joke about programming")

print(result.content)