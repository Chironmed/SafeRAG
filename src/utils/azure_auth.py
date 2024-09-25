import os
import msal
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get environment variables
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
TENANT_ID = os.getenv('TENANT_ID')
AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
SCOPE = ["https://graph.microsoft.com/.default"]

def get_access_token():
    app = msal.ConfidentialClientApplication(
        CLIENT_ID, authority=AUTHORITY,
        client_credential=CLIENT_SECRET
    )
    result = app.acquire_token_silent(SCOPE, account=None)
    if not result:
        result = app.acquire_token_for_client(scopes=SCOPE)
    if "access_token" in result:
        return result["access_token"]
    else:
        print(result.get("error"))
        print(result.get("error_description"))
        print(result.get("correlation_id"))
        return None

def get_user_groups(access_token, user_email):
    graph_url = f"https://graph.microsoft.com/v1.0/users/{user_email}/memberOf"
    headers = {'Authorization': 'Bearer ' + access_token}
    response = requests.get(graph_url, headers=headers)
    if response.status_code == 200:
        groups = response.json().get('value', [])
        return [group['displayName'] for group in groups]
    else:
        # print(f"Error: {response.status_code}, {response.text}")
        return []