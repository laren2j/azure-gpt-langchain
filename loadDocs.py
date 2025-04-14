import os

from langchain_community.vectorstores.azuresearch import AzureSearch
from langchain_openai import AzureOpenAIEmbeddings, OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
import asyncio

# Azure OpenAI Configuration
# These variables are used to configure the Azure OpenAI service.
# Replace the empty strings with your Azure OpenAI endpoint, API key, and deployment details.
azure_endpoint: str = ""  # Azure OpenAI endpoint URL
azure_openai_api_key: str = ""  # Azure OpenAI API key
azure_openai_api_version: str = "2023-05-15"  # API version for Azure OpenAI
azure_deployment: str = ""  # Deployment name for Azure OpenAI

# Azure AI Search Configuration
# These variables are used to configure the Azure Cognitive Search service.
# Replace the empty strings with your Azure Search endpoint and key.
vector_store_address: str = ""  # Azure Cognitive Search endpoint URL
vector_store_password: str = ""  # Azure Cognitive Search API key

# Initialize Azure OpenAI Embeddings
# This object is used to generate embeddings for documents and queries.
embeddings: AzureOpenAIEmbeddings = AzureOpenAIEmbeddings(
    azure_deployment=azure_deployment,
    openai_api_version=azure_openai_api_version,
    azure_endpoint=azure_endpoint,
    api_key=azure_openai_api_key,
)

# Azure Cognitive Search Index Name
# Specify the name of the index in Azure Cognitive Search where documents will be stored.
index_name: str = "azurelangchainrag"

# Async Wrapper Function
# This function initializes the AzureSearch vector store with the provided configuration.
async def wrapper():
    """
    Initializes the AzureSearch vector store with the specified configuration.

    Returns:
        AzureSearch: An instance of the AzureSearch vector store.
    """
    vector_store: AzureSearch = AzureSearch(
        azure_search_endpoint=vector_store_address,
        azure_search_key=vector_store_password,
        index_name=index_name,
        embedding_function=embeddings.embed_query,
    )
    return vector_store

# Initialize the AzureSearch Vector Store
# This runs the async wrapper function to create the vector store instance.
vector_store = asyncio.run(wrapper())

# File Path to the PDF Document
# Specify the path to the PDF document to be loaded and processed.
file_path = "../data/getting-started-oracle-integration-3.pdf"

# Load the PDF Document
# PyPDFLoader is used to load the content of the specified PDF file.
loader = PyPDFLoader(file_path)

# Load the documents from the PDF file.
documents = loader.load()

# Split the Documents into Chunks
# CharacterTextSplitter is used to split the documents into smaller chunks for processing.
# chunk_size: Maximum number of characters in each chunk.
# chunk_overlap: Number of overlapping characters between consecutive chunks.
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

# Add the Document Chunks to the Vector Store
# The processed document chunks are added to the AzureSearch vector store.
vector_store.add_documents(documents=docs)