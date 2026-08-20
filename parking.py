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

# Fixed input
print("Parking Fee:", p.entry(
    "TN01AB1234", "Car", 3, False, True, False, False
))
