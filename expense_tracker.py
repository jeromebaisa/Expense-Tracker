import csv
from pathlib import Path

def add_expense(expenses, description, amount, category, spending_type):
    """Add an expense to the expense records."""
    expense = {
        "description": description,
        "amount": amount,
        "category": category,
        "spending_type": spending_type

    }
    expenses.append(expense)
    return expenses

def calculate_total(expenses):
    """Caluclate the total amount that was spent."""
    return sum(expense["amount"] for expense in expenses)

def summarize_by_category(expenses):
    """Group expenses by category"""
    totals = {}

    for expense in expenses:
        category  = expense["category"]
        totals[category] = totals.get (category, 0) + expense["amount"]

    return totals

def summarize_by_spending_type(expenses):
    """Calculate total spending for Needs, Wants, and Impulse purchases."""

    totals = {
        "Need": 0,
        "Want": 0,
        "Impulse": 0
    }

    for expense in expenses:
        spending_type = expense["spending_type"]
        totals[spending_type] += expense["amount"]

    return totals


# Save expenses to a CSV file
def save_expenses(expenses):
    file_path = Path(__file__).parent / "expenses.csv"

    with open(file_path, "w", newline="") as file:
        fieldnames = ["description", "amount", "category", "spending_type"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(expenses)


# Load saved expenses from a CSV file
def load_expenses():
    file_path = Path(__file__).parent / "expenses.csv"

    expenses = []

    try:
        with open(file_path, "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                expenses.append({
                    "description": row["description"],
                    "amount": float(row["amount"]),
                    "category": row["category"],
                    "spending_type": row["spending_type"]
                })

    except FileNotFoundError:
        return []

    return expenses
