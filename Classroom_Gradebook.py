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

