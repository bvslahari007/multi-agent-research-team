import re


GENRES = {
    "technical": ["ai", "machine", "model", "algorithm", "system", "software", "data"],
    "social": ["education", "society", "culture", "health", "community"],
    "ethical": ["ethics", "policy", "governance", "law", "regulation"],
    "personal": ["my", "me", "i", "name", "life"]
}


def contains_word(text, word):
    return re.search(rf"\b{re.escape(word)}\b", text) is not None


def detect_genre(topic):
    t = topic.lower()

    if any(contains_word(t, k) for k in GENRES["personal"]):
        return "personal"

    if any(contains_word(t, k) for k in GENRES["technical"]) and \
       any(contains_word(t, k) for k in GENRES["social"]):
        return "interdisciplinary"

    if any(contains_word(t, k) for k in GENRES["technical"]):
        return "technical"

    if any(contains_word(t, k) for k in GENRES["social"]):
        return "social"

    if any(contains_word(t, k) for k in GENRES["ethical"]):
        return "ethical"

    return "general"


def run_research(topic, context=None):

    genre = detect_genre(topic)

    dimensions = [
        "relevance and motivation",
        "primary analytical dimensions",
        "stakeholder perspectives",
        "constraints and risks"
    ]

    insights = []

    for dimension in dimensions:
        sentence = (
            f"In analysing {topic}, the dimension of {dimension} becomes central. "
            f"This enables structured reasoning rather than surface-level commentary."
        )

        if context:
            sentence += f" The scope is further shaped by the context of {context}."

        insights.append(sentence)
 
    if "ai" in topic.lower():
        insights.append(
            "Recent developments in foundation models, automation of knowledge work, "
            "and regulatory debates significantly influence the future trajectory of AI systems."
        )

    assumptions = [
        "This exploration focuses on structured conceptual reasoning rather than verified empirical claims.",
        "Interpretations may evolve under specialised domain evidence."
    ]

    return {
        "genre": genre,
        "insights": insights,
        "assumptions": assumptions
    }