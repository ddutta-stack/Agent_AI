from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
# from langchain_community.vectorstores import Chroma -->Ignoring as we are not creating any expternal DB
from langchain.vectorstores import inMemory

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
        vector_store = inMemory.inMemoryvectorstore(embeddings=embeddings)
        # Add the texts to the vectorstore  
    def get_vector_store(self):
        return self.vector_store
    # Next will create an agent