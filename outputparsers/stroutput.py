from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

# Initialize the language model
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

# First prompt template
template1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"]
)

# Second prompt template
template2 = PromptTemplate(
    template="Summarize the following report in bullet points:\n\n{report}",
    input_variables=["report"]
)

# Format the first prompt
prompt1 = template1.format_prompt(topic="The impact of AI on modern education")

# Invoke the language model with the first prompt
result = llm.invoke(prompt1)

# Format the second prompt using the result of the first invocation
prompt2 = template2.format_prompt(report=result.content)

# Invoke the language model with the second prompt
result2 = llm.invoke(prompt2)

# Print the final result
print("\nSummary in Bullet Points:\n", result2.content)