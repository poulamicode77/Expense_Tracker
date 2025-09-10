
import os

EXPENSE_FILE = "expenses.txt"

def add_expense():
    category = input("Enter category (e.g., Food, Travel): ")
    amount = input("Enter amount: ")
    with open(EXPENSE_FILE, "a") as f:
        f.write(f"{category},{amount}\n")
    print("Expense added!")

def view_total():
    total = 0
    if os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, "r") as f:
            for line in f:
                try:
                    _, amount = line.strip().split(",")
                    total += float(amount)
                except ValueError:
                    continue
    print(f"Total expenses: ₹{total:.2f}")

def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Total Expenses")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_total()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
