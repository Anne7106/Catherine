class ParkingManagement:

    slots = {
        "Bike": 2,
        "Car": 2,
        "SUV": 1,
        "Truck": 1,
        "Electric Vehicle": 1
    }

    rates = {
        "Bike": 20,
        "Car": 50,
        "SUV": 70,
        "Truck": 100,
        "Electric Vehicle": 60
    }

    vehicles = []

    def entry(self, vehicle, vtype, hours, vip=False, peak=False,
              lost=False, charging=False):

        if vehicle in self.vehicles:
            return "Duplicate Vehicle"

        if vtype not in self.slots:
            return "Wrong Vehicle Type"

        if self.slots[vtype] <= 0:
            return "Parking Full"

        self.slots[vtype] -= 1
        self.vehicles.append(vehicle)

        fee = self.rates[vtype] * hours

        if peak:
            fee *= 1.5

        if vip:
            fee *= 0.8

        if lost:
            fee += 200

        if charging and vtype == "Electric Vehicle":
            fee += 100

        if hours >= 24:
            fee += 100

        return round(fee, 2)


p = ParkingManagement()

tests = [
    ("V1", "Bike", 2, False, False, False, False),
    ("V2", "Car", 3, False, False, False, False),
    ("V3", "SUV", 4, False, False, False, False),
    ("V4", "Truck", 5, False, False, False, False),
    ("V5", "Electric Vehicle", 3, False, False, False, True),
    ("V6", "Car", 2, True, False, False, False),
    ("V7", "Bike", 3, False, True, False, False),
    ("V8", "Car", 1, False, False, True, False),
    ("V2", "Car", 2, False, False, False, False),
    ("V9", "SUV", 25, False, False, False, False),
    ("V10", "Electric Vehicle", 5, False, True, False, True),
    ("V11", "Bike", 1, False, False, False, False),
    ("V12", "Car", 4, False, True, False, False),
    ("V13", "Truck", 24, True, False, False, False),
    ("V14", "Electric Vehicle", 2, False, False, False, True),
    ("V15", "Wrong", 2, False, False, False, False),
    ("V16", "Car", 2, False, False, False, False),
    ("V17", "SUV", 2, False, False, False, False),
    ("V18", "Bike", 5, False, True, False, False),
    ("V19", "Electric Vehicle", 24, False, False, True, True)
]

for i, test in enumerate(tests, 1):
    print("Test", i, ":", p.entry(*test))
