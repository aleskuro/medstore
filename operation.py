# operation.py

def display_medicines(medicines):
    print("\n------ Available Medicines --------\n")
    print(f"{'S.N.':<5}{'Name':<25}{'Brand':<20}{'Stock':<10}")
    print("-" * 60)

    for i, med in enumerate(medicines, 1):
        print(f"{i:<5}{med.name:<25}{med.brand:<20}{med.stock:<10}")


def find_medicine(medicines, name):
    for med in medicines:
        if med.name.lower() == name.lower():
            return med
    return None


# ==========================
# RESTOCK
# ==========================
def restock(medicines):
    name = input("Enter medicine name: ")
    med = find_medicine(medicines, name)

    if med:
        qty = int(input("Enter quantity to add: "))
        med.stock += qty
        print("Medicine restocked successfully!")
    else:
        print("Medicine not found!")


# ==========================
# SELL
# ==========================
def sell(medicines):
    name = input("Enter medicine name: ")
    med = find_medicine(medicines, name)

    if med:
        qty = int(input("Enter quantity to sell: "))

        if qty > med.stock:
            print("Not enough stock!")
            return

        med.stock -= qty

        price = 10  # simple fixed price
        total = qty * price

        discount = 0
        if qty > 10:
            discount = total * 0.1

        final = total - discount

        print("\n------ BILL ------")
        print(f"Medicine: {med.name}")
        print(f"Quantity: {qty}")
        print(f"Total: Rs.{total}")
        print(f"Discount: Rs.{discount}")
        print(f"Final: Rs.{final}")

    else:
        print("Medicine not found!")