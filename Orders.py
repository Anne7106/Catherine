class Product:
    def __init__(self, product_id, category, quantity, unit_price, discount, tax):
        self.product_id = product_id
        self.category = category
        self.quantity = quantity
        self.unit_price = unit_price
        self.discount = discount
        self.tax = tax
class OrderManagement:
    products = {
        "P101": {"category": "Electronics", "price": 2000, "stock": 10},
        "P102": {"category": "Clothing", "price": 1000, "stock": 20},
        "P103": {"category": "Books", "price": 500, "stock": 50},
        "P104": {"category": "Grocery", "price": 300, "stock": 30}
    }
    coupons = {
        "SAVE10": 10,
        "SAVE20": 20,
        "WELCOME": 15
    }
    def process_order(self, items, coupon_code=None):
        subtotal = 0
        category_discount = 0
        bulk_discount = 0
        for item in items:
            product_id = item["product_id"]
            quantity = item["quantity"]
            if product_id not in self.products:
                return "Invalid product: " + product_id
            if quantity <= 0:
                return "Invalid quantity for " + product_id
            product = self.products[product_id]
            if quantity > product["stock"]:
                return "Out of stock: " + product_id
            price = product["price"]
            item_total = quantity * price
            subtotal += item_total
            if product["category"] == "Electronics":
                category_discount += item_total * 0.10
            elif product["category"] == "Clothing":
                category_discount += item_total * 0.05
            elif product["category"] == "Books":
                category_discount += item_total * 0.08
            if quantity >= 10:
                bulk_discount += item_total * 0.05
        coupon_discount = 0
        if coupon_code is not None:
            if coupon_code not in self.coupons:
                return "Invalid coupon code"
            coupon_discount = subtotal * self.coupons[coupon_code] / 100
        max_discount = subtotal * 0.30
        total_discount = category_discount + bulk_discount + coupon_discount
        if total_discount > max_discount:
            total_discount = max_discount
        taxable_amount = subtotal - total_discount
        gst = taxable_amount * 0.18
        if taxable_amount >= 5000:
            shipping = 0
        else:
            shipping = 100
        final_amount = taxable_amount + gst + shipping
        return {
            "Subtotal": round(subtotal, 2),
            "Category Discount": round(category_discount, 2),
            "Bulk Discount": round(bulk_discount, 2),
            "Coupon Discount": round(coupon_discount, 2),
            "Total Discount": round(total_discount, 2),
            "GST": round(gst, 2),
            "Shipping": shipping,
            "Final Amount": round(final_amount, 2)
        }
if __name__ == "__main__":
    order = OrderManagement()
    items = [
        {
            "product_id": "P101",
            "quantity": 2
        },
        {
            "product_id": "P102",
            "quantity": 3
        }
    ]
    result = order.process_order(items, "SAVE10")
    print("Order Result")
    print("--------------------")
    if isinstance(result, str):
        print(result)
    else:
        for key, value in result.items():
            print(key + ":", value)
