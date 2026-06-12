from expense_utils import add_expense, get_summary, view_all
while True:
    print("\nexpense tracker")
    print("1. add expense")
    print("2. summary")
    print("3. view all")
    print("4. exit")
    choice = input("enter your choice: ")
    if  choice == "1":
        category = input("enter category: ")
        amount = float(input("enter amount: "))
        add_expense(category, amount)
    elif choice == "2":
        get_summary()
    elif choice == "3":
        view_all()
    elif choice == "4":
        print("thank you")
        break
    else:
        print("invalid choice")