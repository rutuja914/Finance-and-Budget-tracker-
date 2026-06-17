import json
from datetime import datetime

EXPENSE_FILE = 'expenses.json'


def load_expenses():
    """Load expenses from a JSON file."""
    try:
        with open(EXPENSE_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_expenses(expenses):
    """Save expenses to a JSON file."""
    with open(EXPENSE_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)

def add_expense(expenses):
    """Add a new expense."""
    date = input("Enter the date (YYYY-MM-DD): ")
    description = input("Enter the description: ")
    amount = float(input("Enter the amount: "))

    expense = {
        'date': date,
        'description': description,
        'amount': amount
    }

    expenses.append(expense)
    print("Expense added.")


def list_expenses(expenses):
    """List all expenses."""
    if not expenses:
        print("No expenses found.")
        return

    for expense in expenses:
        print(f"Date: {expense['date']}, Description: {expense['description']}, Amount: ${expense['amount']}")


def total_expenses(expenses):
    """Calculate the total of all expenses."""
    total = sum(expense['amount'] for expense in expenses)
    print(f"Total expenses: ${total:.2f}")


def main():
    expenses = load_expenses()

    while True:
        print("\nExpense Tracker")
        print("1. Add expense")
        print("2. List expenses")
        print("3. Total expenses")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_expense(expenses)
            save_expenses(expenses)
        elif choice == '2':
            list_expenses(expenses)
        elif choice == '3':
            total_expenses(expenses)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
