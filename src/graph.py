from langgraph.graph import StateGraph
from answer import generate_answer


# 🔹 PROCESS NODE 
def process_node(state):
    query = state["query"]
    docs = state["docs"]

    
    context = "\n".join([d.page_content for d in docs])

    # answer generate
    answer = generate_answer(context, query)

    return {"answer": answer}


# 🔹 ROUTING LOGIC 
def route_node(state):
    answer = state["answer"]

    if "I don't know" in answer:
        return "hitl"
    else:
        return "output"


# 🔹 GRAPH BUILD
builder = StateGraph(dict)

# nodes add karo
builder.add_node("process", process_node)
builder.add_node("output", lambda x: x)

# 👇 HITL node 
builder.add_node("hitl", lambda x: {
    "answer": "⚠️ This query requires human assistance. Your request has been escalated."
})

# entry point
builder.set_entry_point("process")

# conditional routing
builder.add_conditional_edges(
    "process",
    route_node,
    {
        "output": "output",
        "hitl": "hitl"
    }
)

# compile graph
graph = builder.compile()