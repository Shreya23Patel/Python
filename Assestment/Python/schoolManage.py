class SchoolManagement:
    def __init__(self):
        self.students = {}
        self.student_id = 1

    # New Admission
    def new_admission(self):
        name = input("Enter student name: ")
        age = int(input("Enter age: "))
        std = int(input("Enter class (1-12): "))
        mobile = input("Enter guardian mobile number: ")

        if age < 5 or age > 18:
            print("Age must be between 5 and 18")
            return

        if len(mobile) != 10:
            print("Mobile number must be 10 digits")
            return

        self.students[self.student_id] = {
            "Name": name,
            "Age": age,
            "Class": std,
            "Mobile": mobile
        }

        print("Admission successful. Student ID:", self.student_id)
        self.student_id += 1

    # View Student Details
    def view_student(self):
        sid = int(input("Enter student ID: "))
        if sid in self.students:
            print(self.students[sid])
        else:
            print("Student not found")

    # Update Student Info
    def update_student(self):
        sid = int(input("Enter student ID: "))
        if sid in self.students:
            print("1. Update Mobile")
            print("2. Update Class")
            choice = input("Enter choice: ")

            if choice == "1":
                mobile = input("Enter new mobile number: ")
                if len(mobile) == 10:
                    self.students[sid]["Mobile"] = mobile
                    print("Mobile updated")
                else:
                    print("Invalid mobile number")

            elif choice == "2":
                std = int(input("Enter new class: "))
                self.students[sid]["Class"] = std
                print("Class updated")
        else:
            print("Student not found")

    # Remove Student Record
    def remove_student(self):
        sid = int(input("Enter student ID to remove: "))
        if sid in self.students:
            del self.students[sid]
            print("Student record removed")
        else:
            print("Student not found")


# Main Program (Menu Driven)
school = SchoolManagement()

while True:
    print("\n--- School Management System ---")
    print("1. New Admission")
    print("2. View Student Details")
    print("3. Update Student Info")
    print("4. Remove Student Record")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        school.new_admission()
    elif choice == "2":
        school.view_student()
    elif choice == "3":
        school.update_student()
    elif choice == "4":
        school.remove_student()
    elif choice == "5":
        print("Exiting system...")
        break
    else:
        print("Invalid choice")
