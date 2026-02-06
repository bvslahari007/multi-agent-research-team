import random

GENRES = {
    "technical": ["ai", "machine", "model", "algorithm", "system", "software", "data"],
    "social": ["education", "society", "culture", "health", "community"],
    "ethical": ["ethics", "policy", "governance", "law", "regulation"],
    "personal": ["my", "me", "i ", "name", "life"]
}

def detect_genre(topic):
    t = topic.lower()
    if any(k in t for k in GENRES["personal"]):
        return "personal"
    if any(k in t for k in GENRES["technical"]) and any(k in t for k in GENRES["social"]):
        return "interdisciplinary"
    if any(k in t for k in GENRES["technical"]):
        return "technical"
    if any(k in t for k in GENRES["social"]):
        return "social"
    if any(k in t for k in GENRES["ethical"]):
        return "ethical"
    return "general"

def run_research(topic, context=None):
    genre = detect_genre(topic)

    dimensions = [
        "relevance and motivation",
        "primary dimensions of analysis",
        "stakeholder perspectives",
        "key challenges or constraints",
        "future directions or open questions"
    ]

    genre_lens = {
        "technical": [
            "system scalability",
            "design trade-offs",
            "implementation feasibility",
            "performance bottlenecks",
            "future optimisations"
        ],
        "social": [
            "social impact",
            "institutional response",
            "accessibility concerns",
            "long-term societal effects",
            "adoption challenges"
        ],
        "ethical": [
            "accountability",
            "fairness considerations",
            "regulatory alignment",
            "risk of misuse",
            "governance mechanisms"
        ],
        "interdisciplinary": [
            "interaction between technical and social forces",
            "cross-domain tensions",
            "unintended consequences",
            "alignment challenges",
            "collaborative research opportunities"
        ],
        "personal": [
            "interpretive ambiguity",
            "context dependence",
            "subjective meaning",
            "need for clarification",
            "importance of framing"
        ],
        "general": [
            "conceptual significance",
            "multiple interpretations",
            "broad implications",
            "areas of uncertainty",
            "future exploration paths"
        ]
    }

    rhetorical_patterns = [
        "From a research standpoint, {topic} raises important questions around {lens}, particularly in terms of {dimension}.",
        "One way to approach {topic} is by focusing on its {dimension}, where issues of {lens} become evident.",
        "Research discussions surrounding {topic} frequently highlight {dimension}, especially when considering {lens}.",
        "A closer examination of {topic} reveals that {lens} plays a central role in shaping its {dimension}.",
        "An important consideration in the study of {topic} involves {lens}, which directly affects the {dimension}."
    ]

    selected_dimensions = random.sample(dimensions, k=4)
    selected_lens = random.sample(genre_lens[genre], k=4)

    insights = []

    for dim, lens in zip(selected_dimensions, selected_lens):
        sentence = random.choice(rhetorical_patterns).format(
            topic=topic,
            dimension=dim,
            lens=lens
        )
        if context:
            sentence += f" This perspective is particularly relevant within the context of {context}."
        insights.append(sentence)

    assumptions = [
        "This exploration focuses on conceptual reasoning rather than verified factual claims.",
        "Insights may evolve as the topic is examined under more specific or specialised contexts."
    ]

    return {
        "genre": genre,
        "insights": insights,
        "assumptions": assumptions
    }
