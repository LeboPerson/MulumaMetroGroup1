#Lebohang's code
# Create a list to hold all responses
all_responses = []
# Ask how many participants
num_participants = int(input("How many participants? "))
# Collecting answers from each participant
for i in range(num_participants):
  print(f"\nParticipant {i + 1}'s turn:")
  responses = []
for question in questions:
  answer = input(question + "").strip().lower()
  responses.append(answer)
  all_responses.append(responses)
# Showing what was collected
print("\nAll Responses:")
for idx, response in enumerate(all_responses,1):
  print(f"Participant {idx}: {response}")

#Risana
def tally_responses(responses):
    tally = {}

    for name, answers in responses.items():
        for question, answer in answers.items():
            if question not in tally:
                tally[question] = {}
            if answer not in tally[question]:
                tally[question][answer] = {'count': 0, 'participants': []}
            tally[question][answer]['count'] += 1
            tally[question][answer]['participants'].append(name)

    return tally


if __name__ == "__main__":
    #Samantha
    questions = [
    "Have you previously worked on a coding project? (yes/no)",
    "Should students be allowed to use phones during breaks? (yes/no)",
    "Have you finished all of your homework? (yes/no)",
    "Do you think classroom exams should be open book? (yes/no)",
    "Should homework be limited to weekends only? (yes/no)"
       ]

    responses = {}

    # Allow multiple participants to respond
    while True:
        name = input("Enter your name (or type 'done' to finish): ")
        if name.lower() == "done":
            break

        answers = {}
        for question in questions:
            while True:
                answer = input(f"{question} ").strip().lower()
                if answer in ("yes", "no"):
                    answers[question] = answer
                    break
                else:
                    print("Please answer with 'yes' or 'no'.") #Livhuwane
        responses[name] = answers

    # Tally and print the results
    tally = tally_responses(responses)
    print("\n--- Tally Results ---\n") #Livhuwane
    for question, answers in tally.items():
        print(f"Question: {question}")
        for answer, data in answers.items():
            participants = ', '.join(data['participants'])
            print(f"  Answer: {answer} - Count: {data['count']} (Participants: {participants})")
        print() #Livhuwane
