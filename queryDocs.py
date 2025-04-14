from langchain_community.vectorstores.azuresearch import AzureSearch
from langchain_openai import AzureOpenAIEmbeddings, OpenAIEmbeddings
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


index_name: str = "azure-langchain-rag"
async def wrapper():
    vector_store: AzureSearch = AzureSearch(
        azure_search_endpoint=vector_store_address,
        azure_search_key=vector_store_password,
        index_name=index_name,
        embedding_function=embeddings.embed_query,
        )
    return vector_store

vector_store = asyncio.run(wrapper())

# Perform a hybrid search using the search_type parameter
docs = vector_store.similarity_search(
    query="Accelerators and Adapters in Oracle Integration Cloud",
    k=10,
    # search_type="vector",
)

count = 1
for doc in docs:
    print(str(count)+" ******")
    print(doc)
    count = count + 1