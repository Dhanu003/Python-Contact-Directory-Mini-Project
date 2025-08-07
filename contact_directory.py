#mini project

'''

1.create contact
2.display contact
3. search by name
4.search by mobile number
5. update contact
6.delete contact
7.exit

'''
# Mini Project: Contact Management System

def create_contact():
    name = input("Enter name: ")
    number = input("Enter mobile number: ")

    data = name + " : " + number + "\n"
    fp = open("contacts.txt", "a")            # Opening file in append mode
    fp.write(data)
    fp.close()

    print("Contact saved successfully!")


def display_contact():
    try:
        fp = open("contacts.txt", "r")  # Open in read mode
        contacts = fp.readlines()       # Read all lines into a list
        fp.close()

        if len(contacts) == 0:
            print("No contacts found.")
        else:
            print("\n--- All Contacts ---")
            for contact in contacts:
                print(contact.strip())  # Remove extra newline
    except FileNotFoundError:
        print("No contacts found. File doesn't exist yet.")


def search_name():
    name = input("Enter name to search: ")

    try:
        fp = open("contacts.txt", "r")
        contacts = fp.readlines()
        fp.close()

        for contact in contacts:
            if name.lower() in contact.lower():
                print("Contact found:", contact.strip())
                return  # Exit after finding first match

        print("No contact found with that name.")

    except FileNotFoundError:
        print("Contacts file not found.")


def search_number():
    number = input("Enter mobile number to search: ")

    try:
        fp = open("contacts.txt", "r")
        contacts = fp.readlines()
        fp.close()

        for contact in contacts:
            if number in contact:
                print("Contact found:", contact.strip())
                return

        print("No contact found with that number.")

    except FileNotFoundError:
        print("Contacts file not found.")


def update_contact():
    name = input("Enter the name of the contact to update: ")

    try:
        fp = open("contacts.txt", "r")
        contacts = fp.readlines()
        fp.close()

        fp = open("contacts.txt", "w")  # Open file for writing

        for contact in contacts:
            if name in contact:
                new_name = input("Enter new name: ")
                new_number = input("Enter new number: ")
                data = new_name + " : " + new_number + "\n"
                fp.write(data)
            else:
                fp.write(contact)  # Write unchanged contacts

        fp.close()

        print("Contact updated successfully!")

    except FileNotFoundError:
        print("Contacts file not found.")

def delete_contact():
    name_delete = input("Enter the name of the contact to delete: ")

    try:
        fp = open("contacts.txt", "r")  # Read contacts
        contacts = fp.readlines()
        fp.close()

        fp = open("contacts.txt", "w")  # Open for writing

        for contact in contacts:
            if name_delete not in contact:  # If name doesn't match, write it and if match skipped it. This will automatically get deleted
                fp.write(contact)

        fp.close()

        print("Contact deleted successfully!")

    except FileNotFoundError:
        print("Contacts file not found.")


while True:
    print("\n--- Contact Management System ---")
    print("1. Create contact")
    print("2. Display contact")
    print("3. Search by name")
    print("4. Search by mobile number")
    print("5. Update contact")
    print("6. Delete contact")
    print("7. Exit")

    ch = input("Enter your choice: ")

    if ch == '1':
        create_contact()
    elif ch == '2':
        display_contact()
    elif ch == '3':
        search_name()
    elif ch == '4':
        search_number()
    elif ch == '5':
        update_contact()
    elif ch == '6':
        delete_contact()
    elif ch == '7':
        print("User Exit!!")
        break
    else:
        print("Please enter a valid choice.")







































        
