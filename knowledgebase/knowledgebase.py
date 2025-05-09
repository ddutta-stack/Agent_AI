from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
class KnowledgeBase:
    def __init__(self, pathtopdf):
        loader = PyPDFLoader(pathtopdf)
        documents= loader.load()
        # Initialize the text splitter  
    
        textsplitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len,
            is_separator_regex=False,
        )     
        texts=textsplitter.split_documents(documents)
        # Initialize the embeddings
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transfomers/all-MiniLM-L6-v2",
            model_kwargs={"device": "cpu"},
        )   
        vectorstore = Chroma.from_documents(
            texts,
            embeddings,
            persist_directory="db", # Directory to persist the vectorstore and its stored locally
        )
        # Persist the vectorstore
        vectorstore.persist()   