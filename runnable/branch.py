from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough ,RunnableLambda, RunnableBranch

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

prompt1=PromptTemplate(
    template="write a detailed report on {topic}",
    input_variables=["topic"],
)

prompt2=PromptTemplate(
    template="Summarize the following text: {text}",
    input_variables=["text"],
)

parser=StrOutputParser()

report_chain=RunnableSequence(prompt1 | model | parser)

branch_chain=RunnableBranch(
    (lambda x: len(str(x).split()) > 500, RunnableSequence(prompt2 | model | parser)),
    RunnablePassthrough()
)

final_chain=report_chain | branch_chain

print(final_chain.invoke({"topic": "climate change"}))