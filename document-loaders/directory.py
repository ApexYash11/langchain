from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader= DirectoryLoader(
    "path_to_your_directory",
    glob="**/*.pdf",
    loader_cls=PyPDFLoader
)

docs = loader.load()