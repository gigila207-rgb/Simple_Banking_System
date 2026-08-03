from utils import show_header, show_menu
from bank import (
    check_balance,
    deposit,
    withdraw,
    transaction_history,
)


def main():
    while True:

        show_header()
        show_menu()

        choice = input("\nChoose an option: ")

        if choice == "1":
            check_balance()

        elif choice == "2":
            deposit()

        elif choice == "3":
            withdraw()

        elif choice == "4":
            transaction_history()

        elif choice == "5":
            print("\nThank you for using Python Bank!")
            break

        else:
            print("\nInvalid choice.")
            input("Press Enter to continue...")


if __name__ == "__main__":
    main()
