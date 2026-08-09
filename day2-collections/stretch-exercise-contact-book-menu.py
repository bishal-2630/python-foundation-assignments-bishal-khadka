contacts = {} # Initialize an empty dictionary to store contacts


while True:
    print("\n--- Contact Book ---")
    print("1. Add contact")
    print("2. Search contact")
    print("3. Delete contact")
    print("4. Display all contacts")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    #Add contact
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email address: ")
        contacts[name] = { #creates a nested dictionary 
            "phone": phone,
            "email": email
        }

        print(f"Contact '{name}' added successfully.")

    elif choice == "2": # search user 
        name = input("Enter name to search: ")
        if name in contacts: # check if user exists in contacts
            print(f"Name: {name}")
            print(f"Phone: {contacts[name]['phone']}")
            print(f"Email: {contacts[name]['email']}")
        else:
            print(f"Contact '{name}' not found.")

    elif choice == "3": # delete contact
        name = input("Enter name to delete: ")
        if name in contacts: # check if user exists in contacts
            del contacts[name] # delete user from contacts
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' not found.")

    elif choice == "4": # display all contacts
        if contacts: # check if contacts is not empty
            print("\nAll Contacts:")
            for name, details in contacts.items(): # iterate through contacts dictionary
                print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")
        else:
            print("No contacts found.")

    elif choice == "5":
        print("Exiting contact book...")
        break  # stop the loop and exit the program

    else:
        print("Invalid choice. Please try again.")

# Output:
'''
--- Contact Book ---
1. Add contact
2. Search contact
3. Delete contact
4. Display all contacts
5. Exit
Enter your choice (1-5): 1
Enter name: Bishal
Enter phone number: 9867898034
Enter email address: kbishal177@gmail.com
Contact 'Bishal' added successfully.

--- Contact Book ---
1. Add contact
2. Search contact
3. Delete contact
4. Display all contacts
5. Exit
Enter your choice (1-5): 2
Enter name to search: Bishal
Name: Bishal
Phone: 9867898034
Email: kbishal177@gmail.com

--- Contact Book ---
1. Add contact
2. Search contact
3. Delete contact
4. Display all contacts
5. Exit
Enter your choice (1-5): 3
Enter name to delete: Bishal
Contact 'Bishal' deleted successfully.

--- Contact Book ---
1. Add contact
2. Search contact
3. Delete contact
4. Display all contacts
5. Exit
Enter your choice (1-5): 4

All Contacts:
Name: Bishal, Phone: 9867898034, Email: kbishal177@gmail.com

--- Contact Book ---
1. Add contact
2. Search contact
3. Delete contact
4. Display all contacts
5. Exit
Enter your choice (1-5): 5
Exiting contact book...

--- Contact Book ---
1. Add contact
2. Search contact
3. Delete contact
4. Display all contacts
5. Exit
Enter your choice (1-5): 6
Invalid choice. Please try again.
'''