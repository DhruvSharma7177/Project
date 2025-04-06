def collect_financial_data():
    income = float(input("Enter your monthly income: "))
    savings = float(input("Enter your monthly savings: "))
    categories = ["Food", "Entertainment", "Rent", "Transport", "Others"]
    expenses = {}
    
    for category in categories:
        expenses[category] = float(input(f"Enter your spending on {category}: "))
    
    return income, savings, expenses

income, savings, expenses = collect_financial_data()

def analyze_spending(income, savings, expenses):
    total_expenses = sum(expenses.values())
    print(f"Total Expenses: ${total_expenses:.2f}")
    
    for category, amount in expenses.items():
        percentage = (amount / income) * 100
        print(f"{category}: {percentage:.2f}% of income")
        
        if percentage > 30:
            print(f"⚠️ Warning: High spending on {category}!")

analyze_spending(income, savings, expenses)
