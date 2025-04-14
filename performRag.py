import os

from langchain_community.vectorstores.azuresearch import AzureSearch
from langchain_openai import AzureOpenAIEmbeddings, OpenAIEmbeddings
from langchain_openai import AzureChatOpenAI
import asyncio

# Azure OpenAI Configuration
# These variables are used to configure the Azure OpenAI service.
# Replace the empty strings with your Azure OpenAI endpoint, API key, and deployment details.
azure_endpoint: str = ""  # Azure OpenAI endpoint URL
azure_openai_api_key: str = ""  # Azure OpenAI API key
azure_openai_api_version: str = "2023-05-15"  # API version for Azure OpenAI
azure_deployment: str = ""  # Deployment name for Azure OpenAI

# Set environment variables for Azure OpenAI
# These environment variables are required for the Azure OpenAI SDK to function.
os.environ["AZURE_OPENAI_ENDPOINT"] = azure_endpoint
os.environ["AZURE_OPENAI_API_KEY"] = azure_openai_api_key

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

# Initialize Azure Chat OpenAI
# This object is used to interact with the Azure OpenAI ChatGPT model.
llm = AzureChatOpenAI(
    azure_deployment="chatgpt4o",  # Deployment name for the ChatGPT model
    api_version="2024-12-01-preview",  # API version for the ChatGPT model
    temperature=0,  # Controls the randomness of the output (0 = deterministic)
    max_tokens=None,  # Maximum number of tokens in the response
    timeout=None,  # Timeout for the request
    max_retries=2,  # Number of retries in case of failure
    # Additional parameters can be added here
)

# Azure Cognitive Search Index Name
# Specify the name of the index in Azure Cognitive Search where documents are stored.
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

# Define the Question
# This is the user query for which the system will retrieve relevant documents and generate a response.
question = "Tell me about Recipes and Ingredients."

# Perform a Hybrid Search
# The similarity_search method retrieves the top-k most relevant documents based on the query.
# search_type can be specified to control the type of search (e.g., "vector").
docs = vector_store.similarity_search(
    query=question,
    k=6,  # Number of top documents to retrieve
    # search_type="vector",  # Uncomment to specify the search type
)

# Build the Context from Retrieved Documents
# The retrieved documents are concatenated into a single context string for use in the prompt.
context = ""
count = 0
for doc in docs:
    count += 1
    context += f"{count}: {doc.page_content}\n"

# Define the Prompt
# The prompt instructs the ChatGPT model to answer the question using the provided context.
prompt = f'''You are an Expert Chef. Answer the given question using the context provided.
Question: {question}
Context: {context}
'''

# Generate the Response
# The llm.invoke method sends the prompt to the ChatGPT model and retrieves the response.
result = llm.invoke(prompt)

# Print the Result
# The content of the response is printed to the console.
print(result.content)