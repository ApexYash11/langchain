from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# chat template

chat_template = ChatPromptTemplate([
  ("system", "You are a helpful customber support assistant."),
  MessagesPlaceholder(variable_name="chat_history"),
  ("human", "{user_input}"),
])

chat_history=[]

# loading chat history
with open('chat_history.txt', 'r') as f:
  chat_history.extend(f.readlines())

print(chat_history)

# prompt
prompt= chat_template.invoke({
  "chat_history":chat_history,
  "user_input":"How can I reset my password?"
})

print(prompt)