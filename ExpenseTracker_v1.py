expenses = []
totals = {}
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
                    print("Negative amount is not allowed")
                    print("Expense cannot be added")
                if category in totals:
                    totals[category] += amount
                else:
                    totals[category] = amount
                answer = input("Add more?(y/n): ")
        elif choice == 2:
            print("-----Expenses-----")
            for expense in expenses:
                print(f"{expense["category"]}: {expense["amount"]}")
        elif choice == 3:
            total = 0
            for expense in expenses:
                total += expense["amount"]
            print(f"Total Expense: Rs{total}")
        elif choice == 4:
            for category, amount in totals.items():
                print(f"{category}:  {amount}")
        elif choice == 5:
            print("Thankyou for using the expense tracker")
            break
        else:
            print("Invalid choice! Please choose a number from 1 to 5")
            
    except ValueError:
        print("Invalid choice! Please enter an integer")