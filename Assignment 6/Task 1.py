class Student:
    """
    Represents a student with a name, student ID, and a list of grades.
    """

    def __init__(self, name, student_id):
        """
        Initializes a Student object.

        Args:
            name (str): The full name of the student.
            student_id (str): The unique ID for the student.
        """
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade):
        """
        Adds a single grade to the student's record.

        Args:
            grade (float or int): The grade to be added.
        """
        if isinstance(grade, (int, float)):
            self.grades.append(float(grade))
        else:
            print("Error: Grade must be a number.")

    def get_average_grade(self):
        """
        Calculates and returns the average of the student's grades.

        Returns:
            float: The average grade, or 0.0 if the student has no grades.
        """
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def __repr__(self):
        """
        Provides a developer-friendly string representation of the student.
        """
        return f"Student(name='{self.name}', student_id='{self.student_id}')"


# --- Example Usage ---

# 1. Create a new student instance
student_one = Student("Manu", "2505B04101")
print(f"Created student: {student_one.name} with ID: {student_one.student_id}")

# 2. Add grades to the student's record
student_one.add_grade(88)
student_one.add_grade(92.5)
student_one.add_grade(79)
print(f"Grades for {student_one.name}: {student_one.grades}")

# 3. Calculate and display the average grade
average = student_one.get_average_grade()
print(f"Average grade for {student_one.name}: {average:.2f}")

# 4. Create another student and calculate their average
student_two = Student("Manoj", "2505B04101")
student_two.add_grade(95)
student_two.add_grade(98)
print(f"\nCreated student: {student_two.name} with ID: {student_two.student_id}")
print(f"Grades for {student_two.name}: {student_two.grades}")
average_two = student_two.get_average_grade()
print(f"Average grade for {student_two.name}: {average_two:.2f}")
