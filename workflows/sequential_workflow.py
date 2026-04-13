from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from src.model import model


class State(TypedDict):
    topic: str
    joke: str
    improved_joke: str
    final_joke: str


def generate_joke(state: State):
    msg = model.invoke(
        f"Write a short joke about {state['topic']}"
    )
    return {"joke": msg.content}


def check_punchline(state: State):
    if "?" in state["joke"] or "!" in state["joke"]:
        return "pass"
    return "fail"


def improve_joke(state: State):
    msg = model.invoke(
        f"Make this joke funnier by adding wordplay: {state['joke']}"
    )
    return {"improved_joke": msg.content}


def polish_joke(state: State):
    msg = model.invoke(
        f"Add a surprising twist to this joke: {state['improved_joke']}"
    )
    return {"final_joke": msg.content}


workflow = StateGraph(State)

workflow.add_node("generate_joke", generate_joke)
workflow.add_node("improve_joke", improve_joke)
workflow.add_node("polish_joke", polish_joke)

workflow.add_edge(START, "generate_joke")

workflow.add_conditional_edges(
    "generate_joke",
    check_punchline,
    {
        "fail": "improve_joke",
        "pass": END,
    },
)

workflow.add_edge("improve_joke", "polish_joke")
workflow.add_edge("polish_joke", END)

agent = workflow.compile()