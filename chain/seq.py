from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

# 1st prompt -> detailed report
template1 = PromptTemplate(
    template="Give me a detailed report on {topic}",
    input_variables=["topic"]
)

# 2nd prompt -> summary
template2 = PromptTemplate(
    template="Give me a summary of {topic}",
    input_variables=["topic"]
)
parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke(
    {"topic": "The impact of AI on modern education"}
)
print(result)