class DigitalWallet:

    def __init__(self):
        self.balance = 5000
        self.pin = "1234"
        self.transactions = 0
        self.failed_pins = 0
        self.daily_limit = 10000

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

        self.balance += amount if kind == "Deposit" else -amount
        self.transactions += 1

        if self.transactions > 5:
            return "Fraud: Too Many Transactions"

        return "Transaction Successful"


w = DigitalWallet()

# Fixed input
print(w.transaction(1000, "1234", "Withdraw"))
print("Balance:", w.balance)
