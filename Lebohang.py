# Define the survey questions
questions = [
"Have you previously worked on a coding project? (yes/no)",
"Should students be allowed to use phones during breaks? (yes/no)",
"Have you finished all of your homework? (yes/no)",
"Do you think classroom exams should be open book? (yes/no)",
"Should homework be limited to weekends only? (yes/no)"
]
# Create a list to hold all responses
all_responses = []
# Ask how many participants
num_participants = int(input("How manyparticipants? "))
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