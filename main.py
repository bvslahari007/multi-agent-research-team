from agents.manager_agent import handle_request

print("\nMulti-Agent Research Support System\n")
print(
    "This system supports research-oriented exploration by structuring thinking\n"
    "and demonstrating how multiple agents collaborate through compressed context sharing.\n"
)

topic = input("Enter a topic or idea to explore:\n> ").strip()
while not topic:
    topic = input("Please enter a non-empty topic:\n> ").strip()

context = input(
    "\nOptional: Add scope or focus (press Enter to skip):\n> "
).strip() or None

print("\nProcessing exploration...\n")

while True:
    print("\nChoose an output view:")
    print("1. Structured research exploration")
    print("2. Compressed context summary")
    print("3. Final coordinated output")
    print("4. Everything")
    print("5. Exit")

    choice = input("> ").strip()

    if choice == "5":
        print("\nSession completed.")
        break

    if choice not in {"1", "2", "3", "4"}:
        print("Invalid choice.")
        continue

    result = handle_request(topic, context, choice)

    print("\n" + "=" * 55)

    if result["type"] == "research":
        print(f"Detected genre: {result['content']['genre']}\n")
        for point in result["content"]["insights"]:
            print("- " + point)
        print("\nAssumptions:")
        for a in result["content"]["assumptions"]:
            print("- " + a)

    elif result["type"] == "summary":
        print("Compressed Context Summary\n")
        print(result["content"]["summary"])

    elif result["type"] == "all":
        print("Structured Research Exploration\n")
        for point in result["content"]["research"]["insights"]:
            print("- " + point)
        print("\nCompressed Context Summary\n")
        print(result["content"]["summary"]["summary"])

    else:
        print("Final Coordinated Output\n")
        print(result["content"])

    print("\n" + "=" * 55)
