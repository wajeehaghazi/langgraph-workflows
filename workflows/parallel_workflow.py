from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from src.model import model


class State(TypedDict):
    topic: str
    joke: str
    story: str
    poem: str
    combined_output: str


def call_llm_1(state: State):
    msg = model.invoke(
        f"Write a joke about {state['topic']}"
    )
    return {"joke": msg.content}


def call_llm_2(state: State):
    msg = model.invoke(
        f"Write a short story about {state['topic']}"
    )
    return {"story": msg.content}


def call_llm_3(state: State):
    msg = model.invoke(
        f"Write a short poem about {state['topic']}"
    )
    return {"poem": msg.content}


def aggregator(state: State):
    combined = (
        f"Here is everything about {state['topic']}:\n\n"
        f"STORY:\n{state['story']}\n\n"
        f"JOKE:\n{state['joke']}\n\n"
        f"POEM:\n{state['poem']}"
    )

    return {"combined_output": combined}


parallel_builder = StateGraph(State)

parallel_builder.add_node("call_llm_1", call_llm_1)
parallel_builder.add_node("call_llm_2", call_llm_2)
parallel_builder.add_node("call_llm_3", call_llm_3)
parallel_builder.add_node("aggregator", aggregator)

parallel_builder.add_edge(START, "call_llm_1")
parallel_builder.add_edge(START, "call_llm_2")
parallel_builder.add_edge(START, "call_llm_3")

parallel_builder.add_edge("call_llm_1", "aggregator")
parallel_builder.add_edge("call_llm_2", "aggregator")
parallel_builder.add_edge("call_llm_3", "aggregator")

parallel_builder.add_edge("aggregator", END)

parallel_workflow = parallel_builder.compile()