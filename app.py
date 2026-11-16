import streamlit as st
from expense_tracker import (
    add_expense,
    calculate_total,
    summarize_by_spending_type
)

st.title("Personal Expense Tracker")
st.write("Track your spending and understand your purchasing habits.")

# Store expenses while the app is running
if "expenses" not in st.session_state:
    st.session_state.expenses = []

# Expense entry form
st.subheader("Add an Expense")

with st.form("expense_form"):
    description = st.text_input("Expense Name")

    amount = st.number_input(
        "Amount ($)",
        min_value=0.01,
        value=None,
        step=0.50,
        format="%.2f",
        placeholder="Enter amount (0.00)"
    )
# Dropdown menu for expense category
    category = st.selectbox(
        "Expense Category",
        [
            "Groceries",
            "Food & Drinks",
            "Transportation",
            "Shopping",
            "Entertainment",
            "Bills",
            "Health",
            "Other"
        ],
        index=None,
        placeholder="Select a category"
    )

    spending_type = st.selectbox(
        "Type of Purchase",
        ["Need", "Want", "Impulse"],
        index=None,
        placeholder="Select a spending type"
    )

    submitted = st.form_submit_button("Add Expense")

# Process the expense when submitted
if submitted:
    if not description.strip():
        st.warning("Please enter an expense name.")
    elif amount is None:
        st.warning("Please enter an amount.")
    elif category is None:
        st.warning("Please select an expense category.")
    elif spending_type is None:
        st.warning("Please select a spending type.")
    else:
        add_expense(
            st.session_state.expenses,
            description,
            amount,
            category,
            spending_type
        )
        st.success("Expense added successfully!")

# Display the user's recorded expenses
st.subheader("Your Expenses")

# Check if the user has added any expenses
if st.session_state.expenses:

    # Get the available categories from the saved expenses
    available_categories = sorted(set(
        expense["category"] for expense in st.session_state.expenses
    ))

    # Create a dropdown to filter expenses by category
    selected_category = st.selectbox(
        "Filter by Expense Category",
        available_categories,
        index=None,
        placeholder="Select a category to filter"
    )

    # Create a dropdown to filter expenses by spending type
    selected_type = st.selectbox(
        "Filter by Spending Type",
        ["Need", "Want", "Impulse"],
        index=None,
        placeholder="Select a spending type to filter"
    )

    # Start with all recorded expenses
    filtered_expenses = st.session_state.expenses

    # Filter by category if the user selects one
    if selected_category is not None:
        filtered_expenses = [
            expense for expense in filtered_expenses
            if expense["category"] == selected_category
        ]

    # Filter by spending type if the user selects one
    if selected_type is not None:
        filtered_expenses = [
            expense for expense in filtered_expenses
            if expense["spending_type"] == selected_type
        ]

    # Display the filtered expenses
    if filtered_expenses:

        # Create a list for expenses with formatted amounts
        display_expenses = []

        # Go through each filtered expense
        for expense in filtered_expenses:

            # Copy the expense without changing the original data
            display_expense = {
                "Expense Name": expense["description"].title(),
                "Amount": f"${expense['amount']:,.2f}",
                "Category": expense["category"],
                "Spending Type": expense["spending_type"]
            }

            # Add the formatted expense to the display list
            display_expenses.append(display_expense)

        st.table(display_expenses)

        # Calculate the total of the displayed expenses
        filtered_total = calculate_total(filtered_expenses)
        st.metric("Displayed Spending", f"${filtered_total:,.2f}")

    else:
        st.info("No expenses match the selected filters.")

    # Calculate the total of all recorded expenses
    total = calculate_total(st.session_state.expenses)
    st.metric("Total Spending", f"${total:,.2f}")

else:
    st.info("No expenses added yet.")

# Display the spending breakdown for all recorded expenses
if st.session_state.expenses:
    st.subheader("Spending Breakdown")

    # Calculate totals for each spending type
    spending_totals = summarize_by_spending_type(
        st.session_state.expenses
    )

    # Display the spending totals
    st.write(f"Needs: ${spending_totals['Need']:,.2f}")
    st.write(f"Wants: ${spending_totals['Want']:,.2f}")
    st.write(f"Impulse: ${spending_totals['Impulse']:,.2f}")
