contacts={}
while True:
    choice = input("add/search/delete/list/exit:")
    if choice == "add":
        name=input("enter name:")
        phone=input("enter phone number:")
        contacts[name]=phone
        print(f"{name}added")
    elif choice=="search":
        name=input("enter name:")
        print(f"phone:{contacts.get(name,'contat not found')}")
    elif choice=="delete":
        name=input("enter name:")
        if name in contacts:
            del contacts[name]
            print(f"{name}deleted")
        else:
            print("contact not found")
    elif choice=="list":
        for name in sorted(contacts):
            print(f"{name}:{contacts[name]}")
    elif choice=="exit":
        break
    else:
        print("invalid choice")