import os
import chromadb
from chromadb.config import Settings
from chromadb.utils import embedding_functions
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get environment variables
CHROMA_PERSIST_DIRECTORY = os.getenv('CHROMA_PERSIST_DIRECTORY', './chroma_db')
COLLECTION_NAME = os.getenv('COLLECTION_NAME', 'company_doc')

def get_or_create_persistent_client(persist_directory=CHROMA_PERSIST_DIRECTORY):
    if not os.path.exists(persist_directory):
        os.makedirs(persist_directory)
        print(f"Created directory: {persist_directory}")
    else:
        print(f"Directory already exists: {persist_directory}")
    
    return chromadb.PersistentClient(path=persist_directory, settings=Settings())

def get_or_create_collection(client, collection_name=COLLECTION_NAME):
    embedding_function = embedding_functions.DefaultEmbeddingFunction()
    return client.get_or_create_collection(
        name=collection_name,
        embedding_function=embedding_function
    )

def add_documents_to_collection(collection, documents, metadatas, ids):
    collection.add(
        documents=documents,
        metadatas=metadatas,
        ids=ids
    )
    print(f"Added {len(documents)} documents to Chroma DB.")

def query_collection(collection, query_text, n_results=5):
    return collection.query(
        query_texts=[query_text],
        n_results=n_results
    )

def print_query_results(results):
    print("\nQuery Results:")
    for i, (document, metadata, distance) in enumerate(zip(results['documents'][0], results['metadatas'][0], results['distances'][0])):
        print(f"{i + 1}. Document ID: {results['ids'][0][i]}")
        print(f"   Content: {document[:100]}...")
        print(f"   Metadata: {metadata}")
        print(f"   Distance: {distance}\n")

def get_chroma_client():
    print(CHROMA_PERSIST_DIRECTORY)
    return chromadb.PersistentClient(path=CHROMA_PERSIST_DIRECTORY, settings=Settings())

def get_collection(client):
    return client.get_collection(COLLECTION_NAME)

def query_chroma_db(collection, query, user_groups):
    n_results = 5
    base_query = {
        "query_texts": [query],
        "n_results": n_results
    }

    if not user_groups:
        return collection.query(**base_query)

    access_groups = [group for group in user_groups if group.endswith('_Access')]
    highest_access = max(access_groups, default='L0_Access')

    filter_conditions = {
        "$or": [
            {
                "$and": [
                    {"level": highest_access},
                    {"department": {"$in": user_groups}}
                ]
            },
            {"level": "L0_Access"}
        ]
    }

    base_query["where"] = filter_conditions
    return collection.query(**base_query)

def print_search_results(results):
    print("\nSearch Results:")
    for i, (document, metadata, distance) in enumerate(zip(results['documents'][0], results['metadatas'][0], results['distances'][0])):
        print(f"{i + 1}. Document ID: {results['ids'][0][i]}")
        print(f"   Content: {document[:100]}...")
        print(f"   Metadata: {metadata}")
        print(f"   Distance: {distance}\n")