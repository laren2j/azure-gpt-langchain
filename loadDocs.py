import os

from langchain_community.vectorstores.azuresearch import AzureSearch
from langchain_openai import AzureOpenAIEmbeddings, OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
import asyncio

#Azure OpenAI
azure_endpoint: str = ""
azure_openai_api_key: str = ""
azure_openai_api_version: str = "2023-05-15"
azure_deployment: str = ""

#Azure AI Search
vector_store_address: str = ""
vector_store_password: str = ""

embeddings: AzureOpenAIEmbeddings = AzureOpenAIEmbeddings(
    azure_deployment=azure_deployment,
    openai_api_version=azure_openai_api_version,
    azure_endpoint=azure_endpoint,
    api_key=azure_openai_api_key,
)


index_name: str = "azurelangchainrag"
async def wrapper():
    vector_store: AzureSearch = AzureSearch(
        azure_search_endpoint=vector_store_address,
        azure_search_key=vector_store_password,
        index_name=index_name,
        embedding_function=embeddings.embed_query,
        )
    return vector_store

vector_store = asyncio.run(wrapper())

file_path = "../data/getting-started-oracle-integration-3.pdf"
loader = PyPDFLoader(file_path)



documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

vector_store.add_documents(documents=docs)