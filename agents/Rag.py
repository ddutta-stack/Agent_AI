## To create an agent with a custom LLM wiht below methods
from pydantic import BaseModel
from langgraph.graph import StateGraph
from typing import List, Optional


class RAGState(BaseModel):
    """
    State for the RAG agent.
    """
    # Define the state variables
    query: Optional[str]
    retrieved_documents: Optional[List[str]] 
    llm_response: Optional[str]
def retrieve_similar_docs(state: "RAGState")->RAGState:       
        """
        Define logic to Retrieve similar documents from the knowledge base.
        """
        print("RAGState initialized")
        # Define the state graph
def invoke_llm(state: "RAGState") -> RAGState:
        """
        Define logic to invoke the LLM with the retrieved documents.
        """
        print("LLM invoked")
def process_Result(state: "RAGState") -> RAGState:
        """
        Define logic to process the LLM response.
        """
        print("LLM response processed")

workflow = StateGraph(RAGState)

workflow.add_node("retrieve_similar_docs", retrieve_similar_docs)
workflow.add_node("invoke_llm", invoke_llm)
workflow.add_node("process_Result", process_Result)

workflow.add_edge("retrieve_similar_docs", "invoke_llm")
workflow.add_edge("invoke_llm", "process_Result")

workflow.set_entry_point("retrieve_similar_docs")
rag_graph = workflow.compile()