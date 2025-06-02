
users = 3 #Bob


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

    print(f"📋 Survey starting — max {users} participants allowed.\n")#Bob

    while len(responses) < users:
        print(f"\nParticipant {len(responses) + 1} of {users}")#Lebohang's code
        name = input("Enter your name (or type 'done' to finish): ".strip())
        
        if name.lower() == "done":
            break


        if name in responses:
            print(" This name has already participated. Please use a different name.")#Bob
            continue


        answers = {}
        for question in questions:#Lebohang's code
            while True:
                answer = input(f"{question} ").strip().lower()#Lebohang's code
                if answer in ("yes", "no"):
                    answers[question] = answer
                    break
                else:
                    print("Please answer with 'yes' or 'no'.") #Livhuwane
        responses[name] = answers

    #Bob
    if len(responses) == users:
        print("\n Reached the maximum number of participants.")#Bob

    tally = tally_responses(responses)
    print("\n--- Tally Results ---\n") #Livhuwane
    for question, answers in tally.items():
        print(f"Question: {question}")
        for answer, data in answers.items():
            participants = ', '.join(data['participants'])
            print(f"  Answer: {answer} - Count: {data['count']} (Participants: {participants})")
        print() #Livhuwane
