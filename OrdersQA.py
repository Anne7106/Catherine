class OrderManagement:

    prices = {"P1": 1000, "P2": 500, "P3": 200}
    stock = {"P1": 10, "P2": 20, "P3": 30}

    def process(self, items, coupon=None):
        subtotal = 0

        for pid, qty in items:
            if pid not in self.prices:
                return "Invalid Product"
            if qty <= 0:
                return "Invalid Quantity"
            if qty > self.stock[pid]:
                return "Out of Stock"

            subtotal += self.prices[pid] * qty

        discount = subtotal * 0.10

        if coupon == "SAVE20":
            discount += subtotal * 0.20
        elif coupon not in (None, "SAVE10"):
            return "Invalid Coupon"

        discount = min(discount, subtotal * 0.30)
        gst = (subtotal - discount) * 0.18
        shipping = 0 if subtotal >= 5000 else 100

        return round(subtotal - discount + gst + shipping, 2)


o = OrderManagement()

tests = [
    ([("P1", 1)], None),
    ([("P2", 2)], None),
    ([("P3", 3)], None),
    ([("P1", 2), ("P2", 3)], None),
    ([("P1", 0)], None),
    ([("P1", -1)], None),
    ([("P9", 1)], None),
    ([("P1", 11)], None),
    ([("P1", 2)], "SAVE10"),
    ([("P1", 2)], "SAVE20"),
    ([("P1", 2)], "BAD"),
    ([("P1", 10)], "SAVE20"),
    ([("P2", 5)], None),
    ([("P1", 5)], None),
    ([("P1", 10)], None),
    ([("P2", 10)], None),
    ([("P3", 10)], None),
    ([("P1", 3), ("P2", 4)], "SAVE10"),
    ([("P1", 5), ("P2", 5)], "SAVE20"),
    ([("P1", 10), ("P2", 10)], None)
]

for i, test in enumerate(tests, 1):
    print("Test", i, ":", o.process(test[0], test[1]))
