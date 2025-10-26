from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

loader= PyPDFLoader("Wealthify_conferncepaper[1].pdf")

docs = loader.load()

print(docs[0].page_content)
print(docs[1].metadata)