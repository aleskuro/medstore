# main.py
from read import read_data
from write import save_data
from operation import display_medicines, restock, sell


FILENAME = "data.txt"


def main():
    medicines = read_data(FILENAME)

    while True:
        print("\n===== MEDSTORE MENU =====")
        print("1. View Medicines")
        print("2. Restock Medicines")
        print("3. Sell Medicines")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            display_medicines(medicines)

        elif choice == "2":
            restock(medicines)

        elif choice == "3":
            sell(medicines)

        elif choice == "4":
            save_data(FILENAME, medicines)
            print("Data saved. Goodbye!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()