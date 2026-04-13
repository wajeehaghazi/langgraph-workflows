from typing_extensions import TypedDict, Literal
from langchain.messages import HumanMessage, SystemMessage
from pydantic import BaseModel, Field
from langgraph.graph import StateGraph, START, END
from src.model import model


class Route(BaseModel):
    step: Literal["poem", "story", "joke"] = Field(
        description="Next step"
    )


router = model.with_structured_output(Route)


class State(TypedDict):
    input: str
    decision: str
    output: str


def llm_call_story(state: State):
    result = model.invoke(state["input"])
    return {"output": result.content}


def llm_call_joke(state: State):
    result = model.invoke(state["input"])
    return {"output": result.content}


def llm_call_poem(state: State):
    result = model.invoke(state["input"])
    return {"output": result.content}


def llm_call_router(state: State):
    decision = router.invoke(
        [
            SystemMessage(
                content="Route the input to story, joke, or poem."
            ),
            HumanMessage(
                content=state["input"]
            ),
        ]
    )

    return {"decision": decision.step}


def route_decision(state: State):

    if state["decision"] == "story":
        return "llm_call_story"

    elif state["decision"] == "joke":
        return "llm_call_joke"

    elif state["decision"] == "poem":
        return "llm_call_poem"


router_builder = StateGraph(State)

router_builder.add_node(
    "llm_call_story",
    llm_call_story,
)

router_builder.add_node(
    "llm_call_joke",
    llm_call_joke,
)

router_builder.add_node(
    "llm_call_poem",
    llm_call_poem,
)

router_builder.add_node(
    "llm_call_router",
    llm_call_router,
)

router_builder.add_edge(
    START,
    "llm_call_router",
)

router_builder.add_conditional_edges(
    "llm_call_router",
    route_decision,
    {
        "llm_call_story": "llm_call_story",
        "llm_call_joke": "llm_call_joke",
        "llm_call_poem": "llm_call_poem",
    },
)

router_builder.add_edge("llm_call_story", END)
router_builder.add_edge("llm_call_joke", END)
router_builder.add_edge("llm_call_poem", END)

router_workflow = router_builder.compile()