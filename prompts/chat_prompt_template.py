from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

chat_template = ChatPromptTemplate([
  ("system", "You are a helpful {domain}assistant."),
  ("human", "explin in simpler terms: {question}"),

])

prompt=chat_template.invoke({
  "domain":"math ",
  "question":"What is the Pythagorean theorem?"
})  

print(prompt)