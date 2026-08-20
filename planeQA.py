class AirlineReservation:

    seats = {"Economy": 5, "Business": 3, "First": 2}
    fares = {"Economy": 3000, "Business": 6000, "First": 10000}

    def book(self, passenger, ptype, seat_class, baggage, days):

        if not passenger:
            return "Invalid Passenger"

        if seat_class not in self.seats:
            return "Invalid Class"

        if self.seats[seat_class] <= 0:
            return "Fully Booked"

        fare = self.fares[seat_class]

        if self.seats[seat_class] <= 2:
            fare += 1000

        if days < 7:
            fare += 500

        if ptype == "Student":
            fare *= 0.9
        elif ptype == "Senior":
            fare *= 0.8

        baggage_charge = max(0, baggage - 15) * 100

        self.seats[seat_class] -= 1

        return round(fare + baggage_charge, 2)


a = AirlineReservation()

tests = [
    ("Anne", "Student", "Economy", 10, 20),
    ("John", "Adult", "Business", 15, 30),
    ("Mary", "Senior", "First", 20, 10),
    ("Tom", "Adult", "Economy", 25, 5),
    ("Alex", "Student", "Business", 10, 20),
    ("Sam", "Adult", "First", 15, 30),
    ("", "Adult", "Economy", 10, 20),
    ("David", "Adult", "Economy", 20, 5),
    ("Lisa", "Senior", "Business", 18, 6),
    ("Peter", "Student", "First", 22, 3),
    ("Emma", "Adult", "Economy", 15, 20),
    ("Robert", "Senior", "Economy", 30, 2),
    ("Sara", "Student", "Business", 25, 4),
    ("James", "Adult", "First", 10, 20),
    ("Anna", "Senior", "Economy", 16, 10),
    ("Chris", "Adult", "Business", 30, 5),
    ("Mark", "Student", "Economy", 20, 6),
    ("Julia", "Adult", "First", 25, 2),
    ("Kevin", "Senior", "Business", 15, 15),
    ("Daniel", "Adult", "Economy", 15, 30)
]

for i, test in enumerate(tests, 1):
    print("Test", i, ":", a.book(*test))
