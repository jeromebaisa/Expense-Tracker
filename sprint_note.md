Make a note of the moment Milestone 1 is reached.

# What runs right now?

My Personal Expense Tracker is set up using Python and Streamlit. At this moment, the app is presented with a simple welcome screen when I run it locally. I have also added some placeholder functions for adding expenses, total expenses and sorting expenses by category. They are not completely matured functions yet as this milestone is about setting up the project.

# What did the spike in the graph show?

As for my risk spike, I experimented with the possibility of using python to work out costs and group them by category. I took the typical living costs of food and transport. This test came up with a total of $46.50, which would include $16.50 for food and $30.00 for transportation. This proved that the expense calculations in the basic mode are applicable to my application.

# What's blocking you?

I was having difficulty installing Streamlit and some errors running my python code. I corrected these problems, and was able to go on. My next task is to link the cost calculations to the Streamlit web interface.

# Is your view different?

The scope of my project has remained unchanged. I'm still going to be making a Personal Expense Tracker where they can add their expenses, categorize them and see how much they've spent on each category. Later, more advanced features will be added.


# Build Sprint 2: Working Demo Path

# 1. Describe the demo path in 3–5 steps.

My Personal Expense Tracker now has a working demo path using Python and Streamlit. I decided to add a new feature where the user can describe their purchase based on how they feel. First, the user opens the application. Next, they enter an expense name and amount, then select a category and whether the purchase is a Need, Want, or Impulse. After clicking Add Expense, the application displays the expense in a table. It also calculates the total spending and shows a breakdown of purchases by spending type.

# 2. What's the roughest part that still works?

The roughest part was connecting the Streamlit form to my expense-tracking functions. I encountered an error when trying to add expenses because I was using the wrong variable with the append function. After fixing the error, I was able to continue testing the application.

# 3. What did you cut this week, and why?

I decided not to add permanent data storage, advanced charts, or budgeting features yet. I wanted to focus on making one complete demo path work reliably before adding more complicated features.

# 4. What's most likely to break during next week's recording?

The biggest concern is that expenses are only stored temporarily using Streamlit's session state. Refreshing or restarting the application may cause the data to disappear. Before recording, I plan to practice the demo using sample expenses and confirm that the totals display correctly.