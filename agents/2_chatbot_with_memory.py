"""
Objective:
1. Use different message types - HumanMessage and AIMessage
2. Maintain a full conversation history using both message types
3. Use llama-3.1-8b-instant model using Langchain's ChatGroq
4. Create a sophisticated conversation loop

Main Goal: Create a form of memory for our agent

"""

from typing import TypedDict, List, Union
from langchain_core.messages import HumanMessage, AIMessage
from langgraph.graph import START, END, StateGraph
from langchain_groq import ChatGroq
from utils.settings import settings
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model=settings.GROQ_TEXT_MODEL, max_tokens=settings.MAX_TOKENS)

class ChatbotState(TypedDict):
    messages : List[Union[HumanMessage, AIMessage]]


def process(state: ChatbotState) -> ChatbotState:
    """ This node will solve the request you input """

    response = llm.invoke(state["messages"])

    state['messages'].append(AIMessage(content=response.content))
    print(f"\nAI response: {response.content}")
    print("CURRENT STATE: ", state["messages"])

    return state

# Creating the graph

graph = StateGraph(ChatbotState)

graph.add_node("process", process)
graph.add_edge(START, "process")
graph.add_edge("process", END)

app = graph.compile()

conversation_history = []

user_input = input("Enter: ")
while user_input != "exit":
    conversation_history.append(HumanMessage(content=user_input))

    result = app.invoke({
        "messages" : conversation_history
    })

    print(result['messages'])
    conversation_history = result['messages']

    user_input = input("Enter: ")

with open("logging.txt", "w") as file:
    file.write("Your conversation begins here: \n")
    for message in conversation_history:
        if isinstance(message, HumanMessage):
            file.write(f"You: {message.content} \n")
        elif isinstance(message, AIMessage):
            file.write(f"AI: {message.content}\n\n")
    file.write("End of conversation.")
print("Connversation saved in logging.txt")