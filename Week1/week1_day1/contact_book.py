contact={}
while True:
    print("\n--- Contact Book ---")
    print("1.Add Contact")
    print("2.Search Contact")
    print("3.Delete Contact")
    print("4.Display All Contacts")
    print("5.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        name=input("Enter contact:")
        number=int(input(f"Enter {name} number:"))
        contact[name]=number 
    elif choice==2:
        name=input("Search contact:")
        if name in contact:
            print(f"{name}:{contact[name]}")
        else:
            print("Contact not found")
    elif choice==3:
        name=input("Enter name to delete:")
        del contact[name]
    elif choice==4:
        if contact:
            for name, number in contact.items():
                print(f"{name} : {number}")
        else:
            print("No contacts")
    elif choice==5:
        break 
    else:
        print("Not a valid option")
        