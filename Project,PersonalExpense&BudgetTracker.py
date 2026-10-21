import json
import os
from datetime import datetime

FILE_NAME = "expenses.json"

def load_data():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_data(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense(expenses):
    try:
        amount = float(input("Enter amount spent (₹): "))
        category = input("Enter category (e.g., Food, Transport, Bills): ").strip().capitalize()
        desc = input("Enter description: ").strip()
        
        # Capture current date automatically in YYYY-MM-DD format
        today_date = datetime.now().strftime("%Y-%m-%d")
        
        expenses.append({
            "date": today_date,
            "amount": amount,
            "category": category,
            "description": desc
        })
        save_data(expenses)
        print("Expense recorded successfully!\n")
    except ValueError:
        print("Invalid amount. Please enter a valid number.\n")

def show_datewise_summary(expenses):
    if not expenses:
        print("No expenses recorded yet.\n")
        return
        
    # Group expenses by date
    grouped_by_date = {}
    for item in expenses:
        date = item["date"]
        if date not in grouped_by_date:
            grouped_by_date[date] = []
        grouped_by_date[date].append(item)
        
    print("\n================ DATE-WISE BREAKDOWN ================")
    total_all_time = 0
    
    # Sort dates chronologically
    for date in sorted(grouped_by_date.keys()):
        daily_items = grouped_by_date[date]
        daily_total = sum(item["amount"] for item in daily_items)
        total_all_time += daily_total
        
        print(f"\n Date: {date} (Total: ₹{daily_total:.2f})")
        for item in daily_items:
            print(f"   • ₹{item['amount']:.2f} | {item['category']} | {item['description']}")
            
    print("=====================================================")
    print(f"Overall Total Spent: ₹{total_all_time:.2f}\n")

def show_monthly_summary(expenses):
    if not expenses:
        print("No expenses recorded yet.\n")
        return
        
    target_month = input("Enter month to filter (YYYY-MM, e.g., 2026-09): ").strip()
    
    monthly_expenses = [item for item in expenses if item["date"].startswith(target_month)]
    
    if not monthly_expenses:
        print(f"No expenses found for the month {target_month}.\n")
        return
        
    monthly_total = sum(item["amount"] for item in monthly_expenses)
    
    # Category summary for the month
    categories = {}
    for item in monthly_expenses:
        cat = item["category"]
        categories[cat] = categories.get(cat, 0) + item["amount"]
        
    print(f"\n================ SUMMARY FOR {target_month} ================")
    print(f"Total Monthly Spending: ₹{monthly_total:.2f}")
    print("\nCategory Breakdown:")
    for cat, amt in categories.items():
        print(f"  - {cat}: ₹{amt:.2f}")
    print("=========================================================\n")

def main():
    expenses = load_data()
    while True:
        print("--- Personal Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Date-Wise Breakdown")
        print("3. View Monthly Summary")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_datewise_summary(expenses)
        elif choice == "3":
            show_monthly_summary(expenses)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()