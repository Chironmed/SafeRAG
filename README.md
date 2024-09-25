# SafeRAG

SafeRAG: Secure Retrieval-Augmented Generation system with Azure AD and ChromaDB.

## Setup, Usage, and Project Details

```bash
# Clone and setup
git clone https://github.com/yourusername/SafeRAG.git
cd SafeRAG

# Conda environment
conda create --name saferag python=3.9
conda activate saferag

# Install dependencies using conda or pip from requirements.txt
conda install --yes --file requirements.txt || pip install -r requirements.txt

# Environment setup
cp .env.example .env
# Edit .env with:
# CLIENT_ID=your_azure_client_id
# CLIENT_SECRET=your_azure_client_secret
# TENANT_ID=your_azure_tenant_id
# CHROMA_PERSIST_DIRECTORY=./chroma_db
# COLLECTION_NAME=company_doc
# DATA_FILE_PATH=src/data/company_documents.json

# Prepare data
# Edit src/data/company_documents.json with your document data

# Initialize ChromaDB
python src/add_documents.py

# Run main script
python src/main.py