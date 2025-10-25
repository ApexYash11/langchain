from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableParallel, RunnableSequence

load_dotenv()

prompt1=PromptTemplate(
    template="generate a tweet about {topic}",
    input_variables=["topic"],
)

prompt2=PromptTemplate(
    template="generate a LinkedIn post about {topic}",
    input_variables=["topic"],
)

# Initialize model
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

# Define output parsers
parser = StrOutputParser()

chain=RunnableParallel({
    "tweet": RunnableSequence(prompt1 | model | parser),
    "linkedin": RunnableSequence(prompt2 | model | parser),
})

print(chain.invoke({"topic": "LangChain"}))