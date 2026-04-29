# READ DATA FROM FILE
def read_data():
    data = []

    try:
        with open("data.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",")

                medicine = {
                    "name": parts[0],
                    "brand": parts[1],
                    "stock": int(parts[2])
                }

                data.append(medicine)

    except FileNotFoundError:
        print("Data file not found!")

    return data





# MAIN FUNCTION
def main():
    data = read_data()
    # display_medicines(data)


# RUN PROGRAM
main()
