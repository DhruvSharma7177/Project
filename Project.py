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

def give_financial_advice(income, savings, expenses):
    if savings < (0.2 * income):
        print("💡 Advice: Try to save at least 20% of your income.")
    
    for category, amount in expenses.items():
        if (amount / income) > 0.4:
            print(f"💡 Consider reducing {category} expenses to below 20%.")
    
give_financial_advice(income, savings, expenses)

while True:
    income, savings, expenses = collect_financial_data()
    analyze_spending(income, savings, expenses)
    give_financial_advice(income, savings, expenses)
    
    repeat = input("Do you want to enter another month’s data? (yes/no): ").strip().lower()
    if repeat != 'yes':
        break

import openai

def get_motivational_tip():
    openai.api_key = "OpenAi_API_Key"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "Give a motivational money-saving tip."}]
    )

    return response["choices"][0]["message"]["content"]

print("💰 Motivation:", get_motivational_tip())
