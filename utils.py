import os


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    input("\nPress Enter to continue...")


def show_header():
    clear_screen()

    print("=" * 45)
    print("             🏦 PYTHON BANK")
    print("=" * 45)


def show_menu():
    print("\nWelcome to your account!\n")

    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transaction History")
    print("5. Exit")
