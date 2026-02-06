from agents.research_agent import run_research
from agents.summariser_agent import summarize

def handle_request(topic, context, choice):
    research = run_research(topic, context)
    summary = summarize(research)

    if choice == "1":
        return {"type": "research", "content": research}
    if choice == "2":
        return {"type": "summary", "content": summary}
    if choice == "4":
        return {"type": "all", "content": {"research": research, "summary": summary}}
    return {"type": "final", "content": summary["summary"]}
