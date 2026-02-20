from agents.manager_agent import handle_request


def get_non_empty_input(prompt):
    value = input(prompt).strip()
    while not value:
        value = input("Please enter a non-empty value:\n> ").strip()
    return value


def display_research(content):
    print(f"\nDetected Genre: {content['genre']}\n")
    print("Research Insights:\n")
    for point in content["insights"]:
        print(f"- {point}")
    print("\nAssumptions:\n")
    for assumption in content["assumptions"]:
        print(f"- {assumption}")


def display_summary(content):
    print("\nCompressed Context Summary:\n")
    print(content["summary"])


def display_critique(content):
    print("\nCritic Evaluation:\n")
    print(f"Score: {content['score']}/3\n")
    print("Feedback:")
    for item in content["feedback"]:
        print(f"- {item}")


def display_complete(state):
    print("\n=== FULL SYSTEM STATE ===\n")

    print("Research Insights:")
    for point in state["research"]["insights"]:
        print(f"- {point}")

    print("\nCritic Score:", state["critique"]["score"])
    print("Critic Feedback:")
    for item in state["critique"]["feedback"]:
        print(f"- {item}")

    print("\nFinal Summary:\n")
    print(state["summary"]["summary"])


if __name__ == "__main__":

    print("\nMulti-Agent Research Support System\n")
    print(
        "This system demonstrates coordinated multi-agent reasoning\n"
        "with research generation, evaluation, and API-based compression.\n"
    )

    topic = get_non_empty_input("Enter a topic or idea to explore:\n> ")

    context = input(
        "\nOptional: Add scope or focus (press Enter to skip):\n> "
    ).strip() or None

    print("\nProcessing exploration...\n")

    while True:
        print("\nChoose an output view:")
        print("1. Structured research exploration")
        print("2. Compressed context summary (API)")
        print("3. Critic evaluation")
        print("4. Complete system state")
        print("5. Exit")

        choice = input("> ").strip()

        if choice == "5":
            print("\nSession completed.")
            break

        if choice not in {"1", "2", "3", "4"}:
            print("Invalid choice.")
            continue

        result = handle_request(topic, context, choice)

        print("\n" + "=" * 60)

        if result["type"] == "research":
            display_research(result["content"])

        elif result["type"] == "summary":
            display_summary(result["content"])

        elif result["type"] == "critique":
            display_critique(result["content"])

        elif result["type"] == "complete":
            display_complete(result["content"])

        print("\n" + "=" * 60)