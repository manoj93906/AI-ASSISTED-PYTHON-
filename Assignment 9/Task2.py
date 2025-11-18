class Student:
    # MANUAL COMMENT: Initialize student attributes: name, roll number, and hostel status.
    def __init__(self, name, roll_no, hostel_status):
        # MANUAL COMMENT: Assign the student's name to self.name
        self.name = name
        # MANUAL COMMENT: Assign the student's roll number to self.roll_no
        self.roll_no = roll_no
        # MANUAL COMMENT: Assign the hostel status ("hostel" or "non-hostel") to self.hostel_status
        self.hostel_status = hostel_status
        # MANUAL COMMENT: Set the fee based on the student's hostel status.
        if self.hostel_status.lower() == "hostel":
            self.fee = 50000  # Example default fee for hostel students
        else:
            self.fee = 30000  # Example default fee for non-hostel students

    # MANUAL COMMENT: Method to update fee structure depending on hostel status.
    def fee_update(self):
        # MANUAL COMMENT: Check hostel status and update the fee attribute accordingly.
        if self.hostel_status.lower() == "hostel":
            self.fee = 55000  # Updated fee for hostel students
        else:
            self.fee = 35000  # Updated fee for non-hostel students

    # MANUAL COMMENT: Method to print all student details in a formatted way.
    def display_details(self):
        # MANUAL COMMENT: Print the student name, roll number, hostel status, and current fee.
        print("Student Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Hostel Status:", self.hostel_status)
        print("Current Fee:", self.fee)

# AI-GENERATED COMMENTS (using e.g., GitHub Copilot, marked with // AI:):
class Student:
    # AI: Initializes a new Student object with name, roll_no, and hostel_status.
    def __init__(self, name, roll_no, hostel_status):
        # AI: Assigns the provided name to the Student.
        self.name = name
        # AI: Stores the roll number of the Student.
        self.roll_no = roll_no
        # AI: Saves whether the student is a hostel or non-hostel student.
        self.hostel_status = hostel_status
        # AI: Sets the initial fee based on hostel status.
        if self.hostel_status.lower() == "hostel":
            self.fee = 50000
        else:
            self.fee = 30000

    # AI: Updates the student's fee based on their hostel status.
    def fee_update(self):
        # AI: Checks hostel status and updates the fee to the corresponding value.
        if self.hostel_status.lower() == "hostel":
            self.fee = 55000
        else:
            self.fee = 35000

    # AI: Displays the student's details: name, roll number, hostel status, and fee.
    def display_details(self):
        # AI: Prints the relevant information for the student.
        print("Student Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Hostel Status:", self.hostel_status)
        print("Current Fee:", self.fee)


# Collect user input to create a Student object and demonstrate functionality
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")
hostel_status = input("Enter Hostel Status (hostel/non-hostel): ")
student = Student(name, roll_no, hostel_status)

print("\nStudent details before fee update:")
student.display_details()

student.fee_update()

print("\nStudent details after fee update:")
student.display_details()

"""
Comparison:

Manual comments provide detailed logical explanations and reasoning for each code segment, aiding understanding for beginners or those seeking context. AI-generated comments, while mostly correct and complete, tend to focus on summarizing each line or block's immediate effect, sometimes lacking deeper context. Manual comments are slightly more effective for educational clarity, but AI comments are concise and sufficient for familiar readers. Combining both approaches offers maximum value for learning and maintenance.
"""
