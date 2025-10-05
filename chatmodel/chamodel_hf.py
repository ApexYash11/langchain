from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os
import traceback

load_dotenv()

# Accept multiple common env var names so existing .env keys work
hf_token = (
 os.getenv("HUGGINGFACE_API_KEY")

)


llm = HuggingFaceEndpoint(
    model="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation",
    huggingfacehub_api_token=hf_token,
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("Tell me a programming joke.")
print(result.content)


