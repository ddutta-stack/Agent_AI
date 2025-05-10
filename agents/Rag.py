## To create an agent with a custom LLM wiht below methods
from pydantic import BaseModel
from langgraph.graph import StateGraph
from typing import List, Optional


class RAGState(BaseModel):
    """
    State for the RAG agent.
    """
    # Define the state variables
    retrieved_documents: Optional[List[str]]
    llm_response: Optional[str]
    print("RAGState initialized")
    # Define the state graph
