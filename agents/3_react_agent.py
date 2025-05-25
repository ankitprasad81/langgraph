"""
The objective of this project to build a React Agent.

 1. Learn how to create Tools in Langgraph
 2. Jpw to create a React Graph
 3. Work with different types of Messages such as ToolMessage
 4. Test out robustness of our graph

 """

from typing import  TypedDict, Annotated, Sequence
from langchain_groq import ChatGroq
from langchain_core.messages import ToolMessage, BaseMessage, SystemMessage
from langchain_core.tools import tool
from langgraph.graph import StateGraph, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode
from utils.settings import settings
from dotenv import load_dotenv
from IPython.display import Image, display

load_dotenv()

# Reducer function - add_messages
# Rule that controls how updates from nodes are combined with the existing states.
# Tells us how to merge new data into the current state

# Withour reducer, updates would have replaced the existing value entirely

class AgentState(TypedDict):
    messages : Annotated[Sequence[BaseMessage], add_messages]


@tool
def add(a: int, b:int):
    """This is an addition function that adds 2 numbers together"""

    return a + b 

@tool
def subtract(a: int, b: int):
    """Subtraction function"""
    return a - b

@tool
def multiply(a: int, b: int):
    """Multiplication function"""
    return a * b

tools = [add, subtract, multiply]

model = ChatGroq(
    model=settings.GROQ_TEXT_MODEL,
    max_tokens=settings.MAX_TOKENS
).bind_tools(tools)

def model_call(state:AgentState) -> AgentState:
    system_prompt = SystemMessage(content=
        "You are my AI assistant, please answer my query to the best of your ability."
    )
    response = model.invoke([system_prompt] + list(state["messages"]))
    return {"messages": [response]}

def should_continue(state: AgentState): 
    messages = state["messages"]
    last_message = messages[-1]
    if hasattr(last_message, 'tool_calls') and last_message.tool_calls:
        return "continue"
    else:
        return "end"
    

graph = StateGraph(AgentState)
graph.add_node("our_agent", model_call)


tool_node = ToolNode(tools=tools)
graph.add_node("tools", tool_node)

graph.set_entry_point("our_agent")

graph.add_conditional_edges(
    "our_agent",
    should_continue,
    {
        "continue": "tools",
        "end": END,
    },
)

graph.add_edge("tools", "our_agent")

app = graph.compile()

def print_stream(stream):
    for s in stream:
        message = s["messages"][-1]
        if isinstance(message, tuple):
            print(message)
        else:
            message.pretty_print()

inputs = {"messages": [("user", "Add 40 + 12 and then multiply the result by 6. Also tell me a joke please.")]}
print_stream(app.stream(inputs, stream_mode="values"))