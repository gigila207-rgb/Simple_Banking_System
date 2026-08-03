import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    input("\nPress Enter to continue...")


def show_header():
    clear_screen()

    print("=" * 45)
    print("          🏦 PYTHON BANK")
    print("=" * 45)
