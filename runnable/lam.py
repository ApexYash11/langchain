from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough ,RunnableLambda

load_dotenv()

def word_count(text):
    return len(text.split())

prompt=PromptTemplate(
    template="write a joke about {topic}",
    input_variables=["topic"],
)

# Initialize model
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

# Define output parsers
parser = StrOutputParser()

joke_gen_chain=RunnableSequence(prompt | model | parser)

parallel_chain=RunnableParallel({
    "joke": RunnablePassthrough(),
    "word_count": RunnableLambda(word_count)
})

chain=RunnableSequence(joke_gen_chain | parallel_chain)

print(chain.invoke({"topic": "college students"}))