from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

prompt= PromptTemplate(
    template=" Give me a detailed explanation on {topic} ",
    input_variables=["topic"]
)

parser = StrOutputParser()

Chain = prompt | model | parser

result = Chain.invoke({"topic": "Quantum Computing"})



Chain.get_graph().draw_ascii()