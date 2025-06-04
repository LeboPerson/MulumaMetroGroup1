import csv
# Define a Student class to store name and grades

students = {}


class Student:
    def __init__(self,name):
         # Store the student's name
        self.name = name
        self.scores = []          # Create an empty list to store their grades

    def add_score(self, score):
        # Validate the score is between 0 and 100
        if 0 <= score <= 100:
            self.scores.append(score)  # Add the valid score to the student's list
            print(f"Added score {score} for {self.name}.")
        else:
            print("Invalid score! Must be between 0 and 100.")  # Show error if score is invalid
class Gradebook():
    def __init__(self):
       
        self.grades = {}
# Add a new student to the dictionary if they don’t already exist
    def add_student(self,name):
        if name in self.grades:
            print(f"{name} is already in the system.")  # Prevent adding duplicate student
        else:
            self.grades[name] = Student(name)              # Create a new Student object and store it
            print(f"Student {name} added.")             # Confirm student was added

# Record a grade for an existing student
    def record_grade(self,name, score):
        if name in self.grades:
            self.grades[name].add_score(score)  # Call the add_score method from the Student class
        else:
            print(f"{name} not found. Please add the student first.")  # Handle case where student doesn't exist
    #Lebohang's code
    #compute average
    def compute_average(self,name, ):
        if name in self.grades:
            scores = self.grades[name].scores
            if scores:
                return sum(scores) / len(scores)
            else:
                return 0.0  # No scores yet
        else:
            raise ValueError(f"Student '{name}' not found.")
    def class_average(self):
        total_score = 0
        total_count = 0
        
        for student  in self.grades.values():
            total_score += sum(student.scores)
            total_count += len(student.scores)
        
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

    def save_grades(self, filename):
            try:
                with open(filename, 'w', newline='') as file:
                    writer = csv.writer(file)
                    for name, student in self.grades.items():
                        row = [name] + student.scores
                        writer.writerow(row)
                print(f"Grades saved successfully to {filename}.")
            except Exception as e:
                print(f"Error saving grades: {e}")

    def load_grades(self, filename):
            try:
                with open(filename, 'r') as file:
                    reader = csv.reader(file)
                    for row in reader:
                        if row:
                            name = row[0]
                            scores = list(map(float, row[1:]))
                            student = Student(name)
                            for score in scores:
                                if 0 <= score <= 100:
                                    student.add_score(score)
                            self.grades[name] = student
                print(f"Grades loaded successfully from {filename}.")
            except FileNotFoundError:
                print(f"File '{filename}' not found.")
            except Exception as e:
                print(f"Error loading grades: {e}")
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
        print("7. Save Grades to File")
        print("8. Load Grades from File")
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
        elif choice == '7':
            filename = input("Enter filename to save grades (e.g., grades.csv): ")
            gradebook.save_grades(filename)
        elif choice == '8':
            filename = input("Enter filename to load grades (e.g., grades.csv): ")
            gradebook.load_grades(filename)
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
     main()