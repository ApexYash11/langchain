from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

prompt=PromptTemplate(
    template="Summarize the following poem:\n\n{poem}\n\nSummary:",
    input_variables=["poem"]
)
parser=StrOutputParser() 


loader = TextLoader("poem.txt", encoding="utf8")
docs = loader.load()
print(docs)

print(len(docs))

print(docs[0].page_content)

chain=prompt | model | parser

result=chain.invoke({"poem": docs[0].page_content})
print("Summary:", result)
