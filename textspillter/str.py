from langchain.text_splitter import RecursiveCharacterTextSplitter

text="""LangChain is a framework for developing applications powered by language models. It can be used to build chatbots, Generative Question-Answering (GQA) systems, summarization tools, and much more. LangChain provides a standard interface for all LLMs and offers integrations with many of the most popular ones, including OpenAI, Hugging Face, and more. It also provides a suite of tools for working with text data, including prompt management, memory management, and document loading.
d
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0
)

result = splitter.split_text(text)  

print(result[0])
print(len(result))