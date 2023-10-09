class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

contacts = []

def add_contact(name, phone, email, address):
    contacts.append(Contact(name, phone, email, address))

def list_contacts():
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact.name} - {contact.phone}")

def search_contact(query):
    results = []
    for contact in contacts:
        if query in contact.name or query in contact.phone:
            results.append(contact)
    return results

def update_contact(contact_index, name, phone, email, address):
    contact = contacts[contact_index - 1]
    contact.name = name
    contact.phone = phone
    contact.email = email
    contact.address = address

def delete_contact(contact_index):
    del contacts[contact_index - 1]
# Main program starts
while True:
    print("\nContact Book:")
    list_contacts()
    print("\nMenu:")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Update Contact")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter contact name: ")
        phone = input("Enter contact phone number: ")
        email = input("Enter contact email: ")
        address = input("Enter contact address: ")
        add_contact(name, phone, email, address)
    elif choice == "2":
        query = input("Enter a name or phone number to search: ")
        results = search_contact(query)
        if results:
            print("\nSearch Results:")
            for i, result in enumerate(results, start=1):
                print(f"{i}. {result.name} - {result.phone}")
        else:
            print("No matching contacts found.")
    elif choice == "3":
        contact_index = int(input("Enter the contact number to delete: "))
        delete_contact(contact_index)        
    elif choice == "4":
        contact_index = int(input("Enter the contact number to update: "))
        name = input("Enter updated contact name: ")
        phone = input("Enter updated contact phone number: ")
        email = input("Enter updated contact email: ")
        address = input("Enter updated contact address: ")
        update_contact(contact_index, name, phone, email, address)
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")
class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

contacts = []

def add_contact(name, phone, email, address):
    contacts.append(Contact(name, phone, email, address))

def list_contacts():
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact.name} - {contact.phone}")

def search_contact(query):
    results = []
    for contact in contacts:
        if query in contact.name or query in contact.phone:
            results.append(contact)
    return results

def update_contact(contact_index, name, phone, email, address):
    contact = contacts[contact_index - 1]
    contact.name = name
    contact.phone = phone
    contact.email = email
    contact.address = address

def delete_contact(contact_index):
    del contacts[contact_index - 1]
# Main program starts
while True:
    print("\nContact Book:")
    list_contacts()
    print("\nMenu:")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Update Contact")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter contact name: ")
        phone = input("Enter contact phone number: ")
        email = input("Enter contact email: ")
        address = input("Enter contact address: ")
        add_contact(name, phone, email, address)
    elif choice == "2":
        query = input("Enter a name or phone number to search: ")
        results = search_contact(query)
        if results:
            print("\nSearch Results:")
            for i, result in enumerate(results, start=1):
                print(f"{i}. {result.name} - {result.phone}")
        else:
            print("No matching contacts found.")
    elif choice == "3":
        contact_index = int(input("Enter the contact number to delete: "))
        delete_contact(contact_index)        
    elif choice == "4":
        contact_index = int(input("Enter the contact number to update: "))
        name = input("Enter updated contact name: ")
        phone = input("Enter updated contact phone number: ")
        email = input("Enter updated contact email: ")
        address = input("Enter updated contact address: ")
        update_contact(contact_index, name, phone, email, address)
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")
