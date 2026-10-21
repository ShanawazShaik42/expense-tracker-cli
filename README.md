# Personal Expense Tracker

A simple command-line expense tracker written in Python. Record expenses, review spending by date, and see a monthly total with a category breakdown.

## Requirements

- Python 3

## Run the program

Open a terminal in this project folder and run:

```powershell
python "Project,PersonalExpense&BudgetTracker.py"
```

On Windows, you can use the Python launcher if `python` is not available:

```powershell
py "Project,PersonalExpense&BudgetTracker.py"
```

## Menu options

1. **Add Expense** — enter an amount, category, and description. The current date is recorded automatically.
2. **View Date-Wise Breakdown** — review expenses grouped by date, including daily and overall totals.
3. **View Monthly Summary** — enter a month in `YYYY-MM` format to see the monthly total and spending by category.
4. **Exit** — close the program.

## Data storage

Expenses are saved in `expenses.json` in the current working directory. The file is created when the first expense is recorded. Keep a backup of this file if you want to preserve your expense history.
