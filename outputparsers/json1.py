from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

parser = JsonOutputParser()

template= PromptTemplate(
    template=" give me 5 facts about {subject} \n {format_instructions}",
    input_variables=["subject"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

Chain = template | model | parser

result = Chain.invoke({"subject": "the Eiffel Tower"})

print(result)