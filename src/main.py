from utils.azure_auth import get_access_token, get_user_groups
from utils.chroma_utils import get_chroma_client, get_collection, query_chroma_db, print_search_results

def main():
    user_email = input("Enter your email: ")
    query_text = input("Enter your search query: ")

    try:
        # Azure AD authentication
        access_token = get_access_token()
        user_groups = get_user_groups(access_token, user_email)
        print(f"User Groups: {user_groups}")

        # ChromaDB query
        client = get_chroma_client()
        collection = get_collection(client)
        results = query_chroma_db(collection, query_text, user_groups)

        # Display results
        print_search_results(results)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()