import streamlit as st
from expense_tracker import add_expense, calculate_total

st.title("Personal Expense Tracker")
st.write("Track your spending and understand your purchasing habits.")

# Store expenses while the app is running
if "expenses" not in st.session_state:
    st.session_state.expenses = []

# expense entry form
st.subheader("Add an Expense")

with st.form("expense_form"):
    description = st.text_input("Expense Name")

    amount = st.number_input(
        "Amount ($)",
        min_value=0.01,
        step=0.50
    )

    category = st.selectbox(
        "Category",
        ["Food", "Transportation", "Shopping", "Entertainment", "Other"]
    )

    spending_type = st.selectbox(
        "Type of Purchase",
        ["Need", "Want", "Impulse"]
    )

    submitted = st.form_submit_button("Add Expense")

# process the expense when submitted
if submitted:
    if description.strip():
        add_expense(
            st.session_state.expenses,
            description,
            amount,
            category,
            spending_type
        )
        st.success("Expense added successfully!")
    else:
        st.warning("Please enter an expense name.")

#display record expenses
st.subheader("Your Expenses")

if st.session_state.expenses:
    st.table(st.session_state.expenses)

    total = calculate_total(st.session_state.expenses)
    st.metric("Total Spending", f"${total:.2f}")
else:
    st.info("No expenses added yet.")