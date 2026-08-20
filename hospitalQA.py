class HospitalManagement:

    def bill(self, age, appointment, duration, lab, medicine, insurance):
        consultation = duration * 100

        if appointment == "Emergency":
            consultation += 500

        if age >= 60:
            consultation *= 0.8

        if appointment == "Follow-up":
            consultation *= 0.5

        lab_charge = lab * 300
        medicine_charge = medicine * 200
        total = consultation + lab_charge + medicine_charge

        coverage = total * 0.5 if insurance else 0

        return round(total - coverage, 2)


h = HospitalManagement()

tests = [
    (25, "Normal", 1, 1, 1, False),
    (40, "Normal", 2, 2, 2, False),
    (65, "Normal", 2, 2, 2, False),
    (70, "Emergency", 2, 1, 3, False),
    (30, "Emergency", 3, 2, 2, False),
    (60, "Normal", 1, 0, 1, True),
    (75, "Normal", 2, 3, 2, True),
    (45, "Follow-up", 1, 1, 1, False),
    (65, "Follow-up", 2, 2, 2, True),
    (35, "Normal", 3, 0, 0, False),
    (50, "Normal", 1, 3, 0, False),
    (55, "Normal", 1, 0, 5, False),
    (62, "Emergency", 2, 3, 4, True),
    (68, "Follow-up", 1, 0, 2, True),
    (22, "Emergency", 1, 1, 1, True),
    (80, "Normal", 3, 4, 5, True),
    (59, "Normal", 2, 2, 3, False),
    (60, "Emergency", 1, 1, 1, False),
    (45, "Follow-up", 2, 2, 2, True),
    (90, "Emergency", 3, 5, 5, True)
]

for i, t in enumerate(tests, 1):
    print("Test", i, ":", h.bill(*t))
