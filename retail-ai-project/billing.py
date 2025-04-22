def generate_bill(product, customer):
    if not product:
        return "No Product Detected!"
    if not customer:
        return "Customer Not Detected!"

    bill = f"----- BILL -----\n"
    bill += f"Customer : {customer}\n"
    bill += f"Product  : {product}\n"
    bill += f"Total    : ₹100\n"
    bill += f"-----------------\n"
    return bill
