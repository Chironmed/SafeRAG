## SafeRAG

SafeRAG: Secure Retrieval-Augmented Generation system with Azure AD and ChromaDB.

## Setup, Usage, and Project Details


# Clone and setup
```bash
git clone https://github.com/yourusername/SafeRAG.git
cd SafeRAG
```

# Conda environment
```bash
conda create --name saferag python=3.9
conda activate saferag
```

# Install dependencies using conda or pip from requirements.txt
```bash
conda install --yes --file requirements.txt || pip install -r requirements.txt
```

```bash
# Environment setup
cp .env.example .env
```

```env
#Edit .env with:
CLIENT_ID=your_azure_client_id
CLIENT_SECRET=your_azure_client_secret
TENANT_ID=your_azure_tenant_id
CHROMA_PERSIST_DIRECTORY=./chroma_db
COLLECTION_NAME=company_doc
DATA_FILE_PATH=src/data/company_documents.json
```

# Prepare data
# Edit `src/data/company_documents.json` with your document data

```bash
# Initialize ChromaDB
python src/add_documents.py
```

```bash
# Run main script
python src/main.py
```