# Daily-expenses
Daily Expenses

1. Introduction

This document serves as the project report for the Simple Personal Finance Tracker, a foundational command-line application developed in Python. The primary purpose of this script is to help a user monitor, aggregate, and compare their monthly expenses and savings across two consecutive periods (referred to as "Last Month" and "This Month").

2. Project Goal

The main objective of the project is to provide a quick and easy tool for personal financial awareness by:

Collecting detailed expense data across key categories.

Calculating the total expenditure and remaining savings for two periods.

Identifying the largest single expense for each period for comparative analysis.

3. Key Features

The application currently supports the following functional requirements:

Dual-Period Tracking: Accepts input for 8 distinct expense categories for two separate months.

Comprehensive Categories: Tracks standard household and personal expenses, including: Electricity, Water, Grocery, School Fees, Shopping, Internet, OTT Subscriptions, and Medical Bills.

Total Expense Calculation: Automatically sums all input values to provide a total monthly expenditure for both periods.

Savings Calculation: Calculates monthly savings by subtracting the total expenses from a specified monthly salary/income.

Combined Totals: Provides the aggregate total expenses and total savings across both tracked periods.

Maximum Expense Identification: Utilizes list processing and basic iterative logic to find and report the single highest expense item in each month, facilitating easy analysis of spending habits.

4. Technical Implementation

The application is built entirely in Python, leveraging basic data types and control structures.

4.1 Data Input and Storage

The input() function is used to interact with the user via the command line, prompting for specific monetary values.

The int() function is used to ensure all captured inputs are treated as numerical data for accurate calculation.

Variables are named descriptively (e.g., electricity1, water2) to differentiate expenses by category and period.

4.2 Core Logic

The application "Daily Expenses" directly use arithmetic operations for calculating total expenses :

{Total Expenses} = sum {Expenses of all the category}

Savings are calculated relative to a pre-defined salary input:

{Savings} = {Salary} - {Total Expenses}

4.3 Maximum Value Determination

The script determines the maximum expense in each period using a simple loop structure. While standard Python functions like max() exist, the current implementation demonstrates manual iterative comparison, a fundamental programming concept:

Expenses for each month are stored in separate lists (l1, l2).

The first element of the list is initialized as the maximum (a or b).

The loop iterates through every subsequent element, updating the maximum variable if a larger value is encountered.

5. Usage Instructions

To run the application, execute the script in a Python environment. The user will be sequentially prompted to:

Enter the monthly Salary.

Enter the monetary amount for each of the 8 expense categories for the Last Month.

Enter the monetary amount for each of the 8 expense categories for This Month.

Upon receiving all inputs, the application immediately prints the calculated expenses, savings, combined totals, and the maximum expense item for both periods.
Name-Shivam Goyal
