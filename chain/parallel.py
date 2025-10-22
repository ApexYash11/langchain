from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel

load_dotenv()

# Initialize models
model1 = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)
model2 = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)
parser = StrOutputParser()

# 1️⃣ Take notes
template1 = PromptTemplate(
    template="Take notes on the following text:\n{text}",
    input_variables=["text"]
)

# 2️⃣ Generate questions (also from text — not from notes directly)
template2 = PromptTemplate(
    template="Generate 5 questions based on the following text:\n{text}",
    input_variables=["text"]
)

# 3️⃣ Merge
template3 = PromptTemplate(
    template="Merge the following notes and questions into a concise study guide.\n\nNotes:\n{notes}\n\nQuestions:\n{questions}",
    input_variables=["notes", "questions"]
)

# Parallel branch: run both note + question generation
parallel_chain = RunnableParallel({
    "notes": template1 | model1 | parser,
    "questions": template2 | model2 | parser
})

# Merge branch: combine the results
merge_chain = template3 | model2 | parser

# Full pipeline
chain = parallel_chain | merge_chain

# Input text
text = """
Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection.

The advantages of support vector machines are:
- Effective in high dimensional spaces.
- Still effective when number of dimensions > samples.
- Uses subset of training points (support vectors), making it memory efficient.
- Versatile: can use different Kernel functions (linear, RBF, polynomial, etc.)

Disadvantages include:
- Risk of overfitting when features >> samples.
- Doesn’t provide probability estimates directly.
- Requires dense or sparse numpy/scipy data types.
"""

# ✅ Correct invocation
result = chain.invoke({"text": text})

print(result)
