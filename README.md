# SafeRAG

SafeRAG is a secure Retrieval-Augmented Generation system that integrates Azure AD for access control and ChromaDB for document storage and retrieval.

## Setup

1. Clone this repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS and Linux: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Prepare your document data in `src/data/company_documents.json`
6. Run `python src/add_documents.py` to initialize ChromaDB and add documents
7. Run `python src/main.py` to perform a search with access control

## Project Structure

- `src/`: Source code
  - `data/`: Contains the document data
  - `utils/`: Utility functions for Azure AD and ChromaDB
  - `add_documents.py`: Script to add documents to ChromaDB
  - `main.py`: Main script for performing searches
- `config/`: Configuration files
- `requirements.txt`: Python dependencies
- `README.md`: Project documentation
- `.gitignore`: Specifies files to be ignored by Git