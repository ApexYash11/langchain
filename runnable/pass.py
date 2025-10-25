from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough

load_dotenv()

prompt1=PromptTemplate(
    template="write a joke about {topic}",
    input_variables=["topic"],
)

# Initialize model
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

# Define output parsers
parser = StrOutputParser()

prompt2 = PromptTemplate(
    template='Explain the following joke - {text}',
    input_variables=['text']
)

joke_gen_chain=RunnableSequence(prompt1 | model | parser)

parallel_chain=RunnableParallel({
    "joke": RunnablePassthrough(),
   "explanation": RunnableSequence(prompt2 | model | parser)
})

chain=joke_gen_chain | parallel_chain

print(chain.invoke({"topic": "chatgpt"}))