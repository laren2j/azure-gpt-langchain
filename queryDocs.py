import os

from langchain_community.vectorstores.azuresearch import AzureSearch
from langchain_openai import AzureOpenAIEmbeddings, OpenAIEmbeddings
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
# This object is used to generate embeddings for queries and documents.
embeddings: AzureOpenAIEmbeddings = AzureOpenAIEmbeddings(
    azure_deployment=azure_deployment,
    openai_api_version=azure_openai_api_version,
    azure_endpoint=azure_endpoint,
    api_key=azure_openai_api_key,
)

# Azure Cognitive Search Index Name
# Specify the name of the index in Azure Cognitive Search where documents are stored.
index_name: str = "azure-langchain-rag"

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

# Perform a Hybrid Search
# The similarity_search method retrieves the top-k most relevant documents based on the query.
# search_type can be specified to control the type of search (e.g., "vector").
docs = vector_store.similarity_search(
    query="Accelerators and Adapters in Oracle Integration Cloud",  # Query to search for
    k=10,  # Number of top documents to retrieve
    # search_type="vector",  # Uncomment to specify the search type
)

# Display Retrieved Documents
# The retrieved documents are printed to the console with a count for each document.
count = 1
for doc in docs:
    print(str(count) + " ******")  # Print the document number
    print(doc)  # Print the document content
    count += 1  # Increment the document count