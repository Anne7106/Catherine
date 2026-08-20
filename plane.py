class AirlineReservation:

    seats = {"Economy": 5, "Business": 3, "First": 2}
    fares = {"Economy": 3000, "Business": 6000, "First": 10000}

    def book(self, passenger, ptype, seat_class, baggage, days):
        if not passenger:
            print("Invalid Passenger")
            return

        if self.seats[seat_class] <= 0:
            print("Flight Fully Booked")
            return

        fare = self.fares[seat_class]

        # Dynamic pricing
        if self.seats[seat_class] <= 2:
            fare += 1000

        if days < 7:
            fare += 500

        # Passenger discount
        if ptype == "Student":
            fare *= 0.9
        elif ptype == "Senior":
            fare *= 0.8

        baggage_charge = max(0, baggage - 15) * 100

        self.seats[seat_class] -= 1

        print("Passenger       :", passenger)
        print("Class           :", seat_class)
        print("Base Fare       :", self.fares[seat_class])
        print("Dynamic Fare    :", round(fare, 2))
        print("Baggage Charge  :", baggage_charge)
        print("Final Fare      :", round(fare + baggage_charge, 2))
        print("Seat Booked     : Yes")


a = AirlineReservation()

# Fixed input
a.book("Anne", "Student", "Economy", 20, 5)
