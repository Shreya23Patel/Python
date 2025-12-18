class ClinicAppointment:
    def __init__(self):
        self.appointments = {}   # mobile_number : details
        self.time_slots = ["10am", "11am", "12pm", "2pm", "3pm"]

    def book_appointment(self):
        name = input("Enter patient name: ")
        age = int(input("Enter age: "))
        mobile = input("Enter mobile number: ")
        doctor = input("Enter doctor name: ")

        print("Available time slots:")
        for slot in self.time_slots:
            print(slot)

        slot = input("Choose time slot: ")

        # Count appointments for doctor at that slot
        count = 0
        for data in self.appointments.values():
            if data["doctor"] == doctor and data["slot"] == slot:
                count += 1

        if count >= 3:
            print("Slot full for this doctor.")
        else:
            self.appointments[mobile] = {
                "name": name,
                "age": age,
                "doctor": doctor,
                "slot": slot
            }
            print("✅ Appointment booked successfully.")

    def view_appointment(self):
        mobile = input("Enter mobile number: ")
        if mobile in self.appointments:
            data = self.appointments[mobile]
            print("Name:", data["name"])
            print("Age:", data["age"])
            print("Doctor:", data["doctor"])
            print("Time Slot:", data["slot"])
        else:
            print("❌ No appointment found.")

    def cancel_appointment(self):
        mobile = input("Enter mobile number: ")
        if mobile in self.appointments:
            del self.appointments[mobile]
            print("✅ Appointment cancelled.")
        else:
            print("❌ No appointment found.")


# -------- MENU --------
clinic = ClinicAppointment()

while True:
    print("\n--- Clinic Appointment System ---")
    print("1. Book Appointment")
    print("2. View Appointment")
    print("3. Cancel Appointment")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        clinic.book_appointment()
    elif choice == "2":
        clinic.view_appointment()
    elif choice == "3":
        clinic.cancel_appointment()
    elif choice == "4":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")
