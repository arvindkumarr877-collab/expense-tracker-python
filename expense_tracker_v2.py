def add_expenses():
    answer = input("Do you want to add expense(y/n): ")
    while answer.strip().lower() == "y":
        category = input("Enter category: ")
        try:
            amount = int(input("Enter amount: "))  
            if amount<0:
                raise ValueError()
            expense = {"category": category, "amount": amount}
            expenses.append(expense)
            print("Expense added successfully")
        except ValueError:
            print("It is not a positive integer! Please enter a positive integer")
            print("Expense cannot be added")
        answer = input("Add more?(y/n): ")

def view_expenses():
    print("-----Expenses-----")
    if not expenses:
        print("There are no existing expenses")
        
    else:
        for expense in expenses:
            print(f"{expense["category"]}: {expense["amount"]}")

def total_expense():
    total = 0
    for expense in expenses:
        total += expense["amount"]
    print(f"Total Expense: Rs{total}")

def category_expense():
    totals = {}
    for expense in expenses:
        category = expense["category"].strip().upper()
        if category in totals:
            totals[category] += expense["amount"]
        else:
            totals[category] = expense["amount"]
    print("-----Total expenses per category-----")
    for category, amount in totals.items():
                print(f"{category}:  {amount}")
expenses = []
while True: 
    print("-------Expense Tracker-------")
    print("1. Add Expenses")
    print("2. View Expenses")
    print("3. Show Total Expense")
    print("4. Show Category Expenses")
    print("5. Exit")
    try:
        choice = int(input("Enter your choice(1-5): "))
        if choice == 1:
            add_expenses()
        elif choice == 2:
            view_expenses()
        elif choice == 3:
            total_expense()
        elif choice == 4:
            category_expense()
        elif choice == 5:
            print("Thanks for using Expense Tracker")
            break
        else:
            print("Invalid choice! Please enter a number between 1-5")
    except ValueError:
        print("Please enter an integer between 1 to 5")