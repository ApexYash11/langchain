from dotenv import load_dotenv
import os
from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

prompt=PromptTemplate(
    template="Answer the following questions \n {question} from the follwing text - \n {text}:",
    input_variables=["question", "text"]
)
parser=StrOutputParser() 


load_dotenv()

# Set a default USER_AGENT if not already set in the environment
if not os.getenv("USER_AGENT"):
    os.environ["USER_AGENT"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

from langchain_community.document_loaders import WebBaseLoader

url = "https://www.apple.com/in/shop/buy-mac/macbook-air"
loader = WebBaseLoader(url, requests_kwargs={"headers": {"User-Agent": os.getenv("USER_AGENT")}})

docs = loader.load()

chain = prompt | model | parser

print (chain.invoke({
    "question": "What is the price of MacBook Air?",
    "text": docs[0].page_content
}))

