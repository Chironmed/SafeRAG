import json

def load_json_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def prepare_chroma_data(data):
    documents = []
    metadatas = []
    ids = []
    for doc in data['documents']:
        documents.append(doc['content'])
        metadatas.append(doc['metadata'])
        ids.append(doc['id'])
    return documents, metadatas, ids