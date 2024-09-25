import os
from dotenv import load_dotenv
from utils.chroma_utils import get_or_create_persistent_client, get_or_create_collection, add_documents_to_collection, query_collection, print_query_results
from utils.data_utils import load_json_data, prepare_chroma_data

# Load environment variables
load_dotenv()

# Get environment variables
CHROMA_PERSIST_DIRECTORY = os.getenv('CHROMA_PERSIST_DIRECTORY', './chroma_db')
COLLECTION_NAME = os.getenv('COLLECTION_NAME', 'company_doc')
DATA_FILE_PATH = os.getenv('DATA_FILE_PATH', 'src/data/company_documents.json')

def main():
    # Initialize ChromaDB client and collection
    client = get_or_create_persistent_client(CHROMA_PERSIST_DIRECTORY)
    collection = get_or_create_collection(client, COLLECTION_NAME)

    # Load and prepare data
    data = load_json_data(DATA_FILE_PATH)
    documents, metadatas, ids = prepare_chroma_data(data)

    # Add documents to the collection
    add_documents_to_collection(collection, documents, metadatas, ids)

    # Perform a test query
    test_query = "sales strategy and customer feedback for Q4"
    results = query_collection(collection, test_query)
    print_query_results(results)

if __name__ == "__main__":
    main()