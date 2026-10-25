# Personal Expense Tracker

A simple expense tracking application built with Python and Streamlit to help users track their spending habits.

## Features

- Add expenses with a name, amount, and category
- Label purchases as Need, Want, or Impulse
- View recorded expenses
- Calculate total spending
- View spending totals by purchase type

## Technologies

- Python
- Streamlit
- Git and GitHub

## How to Run

1. Install the required packages:
   python3 -m pip install -r requirements.txt

2. Start the application:
   python3 -m streamlit run app.py

3. Open the local URL displayed in the terminal.
## Demo Path

1. Open the Streamlit application.
2. Enter an expense name and amount.
3. Select a category and purchase type.
4. Click "Add Expense".
5. View the expense, total spending, and Need / Want / Impulse breakdown.

## Sample Data

The repository includes `sample_expenses.csv` with example expenses for testing and demonstration. The sample data is not automatically loaded into the application yet.

## Current Status

The basic expense-entry and spending-summary features are implemented. Expenses are stored temporarily during the Streamlit session and are not saved permanently.

Additional features may be added in the future.