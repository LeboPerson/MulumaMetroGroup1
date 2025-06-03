# Define a Student class to store name and grades
class Student:
    def __init__(self, name):
        self.name = name          # Store the student's name
        self.scores = []          # Create an empty list to store their grades

    def add_score(self, score):
        # Validate the score is between 0 and 100
        if 0 <= score <= 100:
            self.scores.append(score)  # Add the valid score to the student's list
            print(f"Added score {score} for {self.name}.")
        else:
            print("Invalid score! Must be between 0 and 100.")  # Show error if score is invalid

# Add a new student to the dictionary if they don’t already exist
def add_student(name):
    if name in students:
        print(f"{name} is already in the system.")  # Prevent adding duplicate student
    else:
        students[name] = Student(name)              # Create a new Student object and store it
        print(f"Student {name} added.")             # Confirm student was added

# Record a grade for an existing student
def record_grade(name, score):
    if name in students:
        students[name].add_score(score)  # Call the add_score method from the Student class
    else:
        print(f"{name} not found. Please add the student first.")  # Handle case where student doesn't exist

#compute average
def compute_average(name, grades):
    if name in grades:
        scores = grades[name]
        if scores:
            return sum(scores) / len(scores)
        else:
            return 0.0  # No scores yet
    else:
        raise ValueError(f"Student '{name}' not found.")
def class_average(grades):
    total_score = 0
    total_count = 0
    
    for scores in grades.values():
        total_score += sum(scores)
        total_count += len(scores)
    
    if total_count == 0:
        return 0.0  # Avoid divide-by-zero
    return total_score / total_count
#highest average
def highest_average(grades):
    highest = None
    highest_avg = -1
    
    for name, scores in grades.items():
        avg = compute_average(name, grades)
        if avg > highest_avg:
            highest_avg = avg
            highest = name
    
    return highest, highest_avg
#lowest average
def lowest_average(grades):
    lowest = None
    lowest_avg = float('inf')
    
    for name, scores in grades.items():
        avg = compute_average(name, grades)
        if avg < lowest_avg:
            lowest_avg = avg
            lowest = name
    
    return lowest, lowest_avg

#Risana's code
def display_student_averages(self):
        print("\nIndividual Student Averages:")
        for name in self.grades:
            average = self.compute_average(name)
            print(f"{name}: {average:.2f}")

   def display_class_average(self):
         average = self.class_average()
         print(f"\nClass Average: {average:.2f}")

   def display_top_bottom_performers(self):
        if not self.grades:
            print("No students in the gradebook.")
            return

        averages = {name: self.compute_average(name) for name in self.grades}
        top_performer = max(averages, key=averages.get)
        bottom_performer = min(averages, key=averages.get)

        print(f"\nTop Performer: {top_performer} with an average of {averages[top_performer]:.2f}")
        print(f"Bottom Performer: {bottom_performer} with an average of {averages[bottom_performer]:.2f}")

   def main():
     gradebook = Gradebook()
#Livhuwane's Code
     while True:
        print("\nMenu:")
        print("1. Add Student")
        print("2. Record Grade")
        print("3. View Student Average")
        print("4. View Class Average")
        print("5. View Top and Bottom Performers")
        print("6. Exit")
#Risana's Code
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter student name: ")
            gradebook.add_student(name)
        elif choice == '2':
            name = input("Enter student name: ")
            score = float(input("Enter score: "))
            gradebook.record_grade(name, score)
        elif choice == '3':
            name = input("Enter student name: ")
            average = gradebook.compute_average(name)
            print(f"{name}'s average: {average:.2f}")
        elif choice == '4':
            gradebook.display_class_average()
        elif choice == '5':
            gradebook.display_top_bottom_performers()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
     main()
