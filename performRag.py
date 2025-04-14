import os

from langchain_community.vectorstores.azuresearch import AzureSearch
from langchain_openai import AzureOpenAIEmbeddings, OpenAIEmbeddings
from langchain_openai import AzureChatOpenAI
import asyncio

#Azure OpenAI
azure_endpoint: str = ""
azure_openai_api_key: str = ""
azure_openai_api_version: str = "2023-05-15"
azure_deployment: str = ""
os.environ["AZURE_OPENAI_ENDPOINT"] = azure_endpoint
os.environ["AZURE_OPENAI_API_KEY"] = azure_openai_api_key

#Azure AI Search
vector_store_address: str = ""
vector_store_password: str = ""


embeddings: AzureOpenAIEmbeddings = AzureOpenAIEmbeddings(
    azure_deployment=azure_deployment,
    openai_api_version=azure_openai_api_version,
    azure_endpoint=azure_endpoint,
    api_key=azure_openai_api_key,
)

llm = AzureChatOpenAI(
    azure_deployment="chatgpt4o",  # or your deployment
    api_version="2024-12-01-preview",  # or your api version
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
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


question = "Tell me about Integration Recipes and Accelerations."


# Perform a hybrid search using the search_type parameter
docs = vector_store.similarity_search(
    query=question,
    k=6,
    # search_type="vector",
)

context = ""

count = 0
for doc in docs:
    count = count + 1
    context = context + str(count)+" :"+doc.page_content+"\n"


# print(context)

prompt = f''' You are Oracle Integration Cloud Expert. Answer the given question using the context provides.
Question: {question}
Context: {context}
'''

# print(prompt)

result = llm.invoke(prompt)

print(result.content)