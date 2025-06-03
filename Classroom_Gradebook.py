class Gradebook:
    def __init__(self):
        self.students = {}  # key: name, value: list of scores

    def add_student(self, name):
        if name in self.students:
            print(f"{name} is already in the system.")
        else:
            self.students[name] = []
            print(f"Student {name} added.")

    def record_grade(self, name, score):
        if name in self.students:
            if 0 <= score <= 100:
                self.students[name].append(score)
                print(f"Added score {score} for {name}.")
            else:
                print("Invalid score! Must be between 0 and 100.")
        else:
            print(f"{name} not found. Please add the student first.")

    def compute_average(self, name):
        if name in self.students:
            scores = self.students[name]
            if scores:
                return sum(scores) / len(scores)
            else:
                return 0.0
        else:
            raise ValueError(f"Student '{name}' not found.")

    def class_average(self):
        total_score = 0
        total_count = 0
        for scores in self.students.values():
            total_score += sum(scores)
            total_count += len(scores)
        return total_score / total_count if total_count > 0 else 0.0

    def highest_average(self):
        highest = None
        highest_avg = -1
        for name in self.students:
            avg = self.compute_average(name)
            if avg > highest_avg:
                highest_avg = avg
                highest = name
        return highest, highest_avg

    def lowest_average(self):
        lowest = None
        lowest_avg = float('inf')
        for name in self.students:
            avg = self.compute_average(name)
            if avg < lowest_avg:
                lowest_avg = avg
                lowest = name
        return lowest, lowest_avg

    def display_student_averages(self):
        print("\nIndividual Student Averages:")
        for name in self.students:
            average = self.compute_average(name)
            print(f"{name}: {average:.2f}")

    def display_class_average(self):
        average = self.class_average()
        print(f"\nClass Average: {average:.2f}")

    def display_top_bottom_performers(self):
        if not self.students:
            print("No students in the gradebook.")
            return
        highest, highest_avg = self.highest_average()
        lowest, lowest_avg = self.lowest_average()
        print(f"\nTop Performer: {highest} with an average of {highest_avg:.2f}")
        print(f"Bottom Performer: {lowest} with an average of {lowest_avg:.2f}")

def main():
    gradebook = Gradebook()
#livhuwane
    while True:
        print("\nMenu:")
        print("1. Add Student")
        print("2. Record Grade")
        print("3. View Student Average")
        print("4. View Class Average")
        print("5. View Top and Bottom Performers")
        print("6. Exit")
#risana
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter student name: ")
            gradebook.add_student(name)
        elif choice == '2':
            name = input("Enter student name: ")
            try:
                score = float(input("Enter score: "))
            except ValueError:
                print("Invalid input for score.")
                continue
            gradebook.record_grade(name, score)
        elif choice == '3':
            name = input("Enter student name: ")
            try:
                average = gradebook.compute_average(name)
                print(f"{name}'s average: {average:.2f}")
            except ValueError as e:
                print(e)
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
