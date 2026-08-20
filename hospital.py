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

        if insurance:
            coverage = total * 0.5
        else:
            coverage = 0

        payable = total - coverage

        print("Consultation Fee :", round(consultation, 2))
        print("Lab Charges      :", lab_charge)
        print("Medicine Charges  :", medicine_charge)
        print("Insurance Cover   :", round(coverage, 2))
        print("Patient Payable   :", round(payable, 2))


h = HospitalManagement()

# Fixed input
h.bill(45, "Normal", 2, 2, 3, False)
