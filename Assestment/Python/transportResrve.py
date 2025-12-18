class BusReservation:
    def __init__(self):
        # Predefined routes with prices
        self.routes = {
            1: ("Mumbai to Pune", 500),
            2: ("Delhi to Jaipur", 600),
            3: ("Ahmedabad to Surat", 400),
            4: ("Goa to Mumbai", 800),
            5: ("Udaipur to Jaipur", 500),
            6: ("Shimla to Manali", 900),
            7: ("Ahmedabad to Banglore", 1000)
        }

        self.tickets = {}   # ticket_id : ticket_details
        self.ticket_id = 1001

    def show_routes(self):
        print("\nAvailable Routes:")
        for key, value in self.routes.items():
            print(key, "-", value[0], "- ₹", value[1])

    def book_ticket(self):
        name = input("Enter passenger name: ")
        age = int(input("Enter age: "))
        mobile = input("Enter mobile number: ")

        self.show_routes()
        choice = int(input("Choose route number: "))

        if choice not in self.routes:
            print("Invalid route!")
            return

        route, price = self.routes[choice]

        # Count seats for this route
        seats_booked = sum(1 for t in self.tickets.values() if t['route'] == route)
        if seats_booked >= 40:
            print("No seats available on this route!")
            return

        seat_no = seats_booked + 1

        self.tickets[self.ticket_id] = {
            "name": name,
            "age": age,
            "mobile": mobile,
            "route": route,
            "price": price,
            "seat": seat_no
        }

        print("\nTicket Booked Successfully!")
        print("Ticket ID:", self.ticket_id)
        print("Seat No:", seat_no)

        self.ticket_id += 1

    def view_ticket(self):
        tid = int(input("Enter Ticket ID: "))
        if tid in self.tickets:
            t = self.tickets[tid]
            print("\nTicket Details:")
            print("Name:", t['name'])
            print("Route:", t['route'])
            print("Seat:", t['seat'])
            print("Price: ₹", t['price'])
        else:
            print("Ticket not found!")

    def cancel_ticket(self):
        tid = int(input("Enter Ticket ID to cancel: "))
        if tid in self.tickets:
            del self.tickets[tid]
            print("Ticket cancelled successfully.")
        else:
            print("Ticket not found!")

    def menu(self):
        while True:
            print("\n--- Bus Reservation Menu ---")
            print("1. Show Routes")
            print("2. Book Ticket")
            print("3. View Ticket")
            print("4. Cancel Ticket")
            print("5. Exit")

            choice = int(input("Enter choice: "))

            if choice == 1:
                self.show_routes()
            elif choice == 2:
                self.book_ticket()
            elif choice == 3:
                self.view_ticket()
            elif choice == 4:
                self.cancel_ticket()
            elif choice == 5:
                print("Thank you for using Bus Reservation System!")
                break
            else:
                print("Invalid choice!")


# Run the system
bus = BusReservation()
bus.menu()
