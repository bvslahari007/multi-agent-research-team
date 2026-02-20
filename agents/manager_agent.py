from agents.research_agent import run_research
from agents.summariser_agent import summarize
from agents.critic_agent import critique


def handle_request(topic, context, choice):

    state = {
        "research": None,
        "critique": None,
        "summary": None
    }

    print("[Manager] Running research agent...")
    state["research"] = run_research(topic, context)

    print("[Manager] Running critic agent...")
    state["critique"] = critique(state["research"])
    print(f"[Manager] Critic score: {state['critique']['score']}/3")
    
    if state["critique"]["score"] < 2:
        print("[Manager] Refining research...")
        state["research"] = run_research(topic, context)
        state["critique"] = critique(state["research"])

    print("[Manager] Running summariser agent...")
    state["summary"] = summarize(state["research"])

    if choice == "1":
        return {"type": "research", "content": state["research"]}

    if choice == "2":
        return {"type": "summary", "content": state["summary"]}

    if choice == "3":
        return {"type": "critique", "content": state["critique"]}

    return {"type": "complete", "content": state}