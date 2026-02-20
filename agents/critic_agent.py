def critique(research_output):

    insights = research_output.get("insights", [])
    score = 0
    feedback = []

    if len(insights) >= 4:
        score += 1
    else:
        feedback.append("Insufficient analytical coverage.")

    detailed = [s for s in insights if len(s.split()) > 18]
    if len(detailed) >= 3:
        score += 1
    else:
        feedback.append("Reasoning depth is limited.")
    
    genre = research_output.get("genre")
    combined = " ".join(insights).lower()

    if genre == "technical":
        if any(term in combined for term in ["model", "system", "automation", "regulation"]):
            score += 1
        else:
            feedback.append("Technical framing lacks domain terminology.")
    else:
        score += 1  

    if not feedback:
        feedback.append("Research quality acceptable.")

    return {
        "score": score,
        "feedback": feedback
    }