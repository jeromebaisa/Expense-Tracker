# Sample expenses
expenses = [
    {"name": "Lunch", "amount": 12.50, "category": "Food"},
    {"name": "Coffee", "amount": 4.00, "category": "Food"},
    {"name": "Gas", "amount": 30.00, "category": "Transportation"}
]

# Calculate total expenses
total = sum(expense["amount"] for expense in expenses)

# Calculate totals by category
category_totals = {}

for expense in expenses:
    category = expense["category"]
    category_totals[category] = (
        category_totals.get(category, 0) + expense["amount"]
    )

# Display results
print("Total Expenses: $", total)
print("Expenses by Category:", category_totals)

# Verify expected results
assert total == 46.50
assert category_totals["Food"] == 16.50
assert category_totals["Transportation"] == 30.00

print("Risk spike passed!")