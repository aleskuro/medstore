# read.py

class Medicine:
    def __init__(self, name, brand, stock):
        self.name = name
        self.brand = brand
        self.stock = stock


def read_data(filename):
    medicines = []

    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split(",")

                med = Medicine(
                    parts[0],
                    parts[1],
                    int(parts[2])
                )

                medicines.append(med)

    except FileNotFoundError:
        print("File not found!")

    return medicines