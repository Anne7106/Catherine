class DigitalWallet:

    def __init__(self):
        self.balance = 5000
        self.pin = "1234"
        self.transactions = 0
        self.failed_pins = 0
        self.daily_limit = 10000
        self.history = []

    def transaction(self, amount, pin, kind):

        if amount <= 0:
            return "Invalid Amount"

        if pin != self.pin:
            self.failed_pins += 1
            if self.failed_pins >= 3:
                return "Fraud: Multiple Failed PINs"
            return "Wrong PIN"

        if amount > self.balance and kind == "Withdraw":
            return "Insufficient Balance"

        if amount > self.daily_limit:
            return "Daily Limit Exceeded"

        if amount > 5000:
            return "Fraud: Large Transaction"

        if amount in self.history:
            return "Duplicate Transaction"

        self.balance += amount if kind == "Deposit" else -amount
        self.transactions += 1
        self.history.append(amount)

        if self.transactions > 5:
            return "Fraud: Too Many Transactions"

        return "Transaction Successful"


w = DigitalWallet()

tests = [
    (1000, "1234", "Withdraw"),
    (10000, "1234", "Withdraw"),
    (12000, "1234", "Deposit"),
    (1000, "1111", "Withdraw"),
    (1000, "2222", "Withdraw"),
    (1000, "3333", "Withdraw"),
    (6000, "1234", "Deposit"),
    (1000, "1234", "Withdraw"),
    (-500, "1234", "Deposit"),
    (500, "1234", "Deposit"),
    (500, "1234", "Deposit"),
    (500, "1234", "Deposit"),
    (500, "1234", "Deposit"),
    (500, "1234", "Deposit"),
    (500, "1234", "Deposit"),
    (500, "1234", "Deposit"),
    (500, "1234", "Deposit"),
    (500, "1234", "Deposit"),
    (500, "1234", "Deposit"),
    (100, "1234", "Withdraw")
]

for i, test in enumerate(tests, 1):
    print("Test", i, ":", w.transaction(*test))
