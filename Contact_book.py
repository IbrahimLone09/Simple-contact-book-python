"""simple program to save contacts of a person.
you can view,search and delete the contact also"""

contacts = {}

print("Welcome to contact book!")

while True:
    print("Type '1' to Add contact:")
    print("Type '2' to View contact:")
    print("Type '3' to Search contact:")
    print("Type '4' to Delete contact:")

    choice = input("Enter your choice (Q to quit!): ").lower()

    if choice == "q":
        print("Exiting contact book!")
        break

    elif choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("Contact added successfully!")

    elif choice == "2":
        if  contacts:
            print("Contacts!")
            for name , phone in contacts.items():
             print(name , ":", phone)

        else:
            print("No contact found!")

    elif choice == "3":
        name = input("Enter name to search: ")
        if name in contacts:
            print("phone number:",contacts[name])

        else:
            print("Contact not found!")

    elif choice == "4":
        name = input("Enter name to delete! ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted!")

        else:
            print("Contact not found!")

    else:
        print("Invalid choice please try again!")
