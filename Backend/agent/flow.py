from typing import Annotated
from typing_extensions import TypedDict
from .nodes.email_generator import message_generator
from .nodes.match_companies import match_companies
from .nodes.resume_parser import resume_parser
from langgraph.graph import StateGraph,START    
from langgraph.graph.message import add_messages 


class State(TypedDict):
    messages:Annotated[list,add_messages]

    resume_file_path:str
    resume_txt:str
    matched_companies:list[dict]
    errors:list[str]
    stage:str

graph_builder=StateGraph(State)

graph_builder.add_node("parse_resume",resume_parser)
graph_builder.add_node("match_companies",match_companies)
graph_builder.add_node("email_generator",message_generator)

graph_builder.add_edge(START,"parse_resume")
graph_builder.add_edge("parse_resume","match_companies")
graph_builder.add_edge("match_companies","email_generator")

graph=graph_builder.compile()


