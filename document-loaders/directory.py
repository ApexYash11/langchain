from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader= DirectoryLoader(
    "path_to_your_directory",
    glob="**/*.pdf",
    loader_cls=PyPDFLoader
)

docs = loader.load()
 
print(f"Loaded {len(docs)} documents.")
for doc in docs:
    print(doc.page_content[:100])  # Print the first 100 characters of each document

# Example usage:
# Make sure to replace "path_to_your_directory" with the actual path to your directory
# containing PDF files.
# This code snippet demonstrates how to use the DirectoryLoader from the langchain_community
# to load all PDF documents from a specified directory and print out the number of documents loaded
# along with the first 100 characters of each document's content.