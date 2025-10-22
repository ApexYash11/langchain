from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

schema=[
    ResponseSchema(name="summary", description="A brief summary of the product review"),
    ResponseSchema(name="sentiment", description="The sentiment of the review, either positive, negative, or neutral"),
    ResponseSchema(name="key_themes", description="A list of key themes mentioned in the review in a list"),
]

parser=StructuredOutputParser.from_response_schemas(schema)

template= PromptTemplate(
    template="Review the following product and provide a structured output.\n{format_instructions}\nProduct Review: {review_text}",
    input_variables=["review_text"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

Chain = template | model | parser
result = Chain.invoke({
    "review_text": """I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.""" 
}) 

print(result)