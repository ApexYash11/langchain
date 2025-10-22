from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda, RunnableBranch
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

# Initialize model
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

# Define Pydantic model
class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(description="The sentiment of the feedback")

# Create Pydantic parser
parser2 = PydanticOutputParser(pydantic_object=Feedback)

# Prompt for sentiment classification
prompt1 = PromptTemplate(
    template=(
        "Classify the sentiment of the following feedback as positive or negative:\n"
        "{feedback}\n"
        "{format_instructions}"
    ),
    input_variables=["feedback"],
    partial_variables={"format_instructions": parser2.get_format_instructions()}
)

# Step 1: Classification chain
classify_chain = prompt1 | model | parser2

# Step 2: Define conditional branches
positive_branch = RunnableLambda(lambda x: f"✅ Positive sentiment detected: {x['feedback']}")
negative_branch = RunnableLambda(lambda x: f"❌ Negative sentiment detected: {x['feedback']}")

# Step 3: Conditional logic using RunnableBranch
branch_chain = RunnableBranch(
    (
        lambda x: x["sentiment"] == "positive", positive_branch
    ),
    (
        lambda x: x["sentiment"] == "negative", negative_branch
    ),
    RunnableLambda(lambda x: f"😐 Neutral or unknown sentiment for: {x['feedback']}")
)

# Step 4: Combine the chain
final_chain = (
    classify_chain
    | RunnableLambda(lambda x: {"sentiment": x.sentiment, "feedback": feedback_text})
    | branch_chain
)

# Input feedback
feedback_text = "The product quality is excellent and I am very satisfied with my purchase!"

# Execute chain
result = final_chain.invoke({"feedback": feedback_text})
print(result)
