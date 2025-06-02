def collect_responses(questions, num_participants):
    all_responses = []
    print("\n--- Survey Time ---\n")
    for i in range(num_participants):
        print(f"\nParticipant {i + 1}, please answer the following questions:")
        participant_responses = {}
        for question in questions:
            answer = input(f"{question} ").strip().lower()
            participant_responses[question] = answer
        all_responses.append(participant_responses)
    return all_responses
