from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence

load_dotenv()

prompt=PromptTemplate(
    template="write a joke about {topic}",
    input_variables=["topic"],
)

# Initialize model
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

# Define output parsers
parser = StrOutputParser()

chain=RunnableSequence(prompt | model | parser)

print(chain.invoke({"topic": "LangChain"}))
