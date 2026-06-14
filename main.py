from contact import Contact
from storage import save_contacts, load_contacts

contacts = load_contacts()

while True:
    print("\n--- Contact Manager ---")
    print("1. Show Contact")
    print("2. Add Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        for contact in contacts:
            print(f"Name: {contact['name']}")
            print(f"Number: {contact['number']}")
            print(f"Email: {contact['email']}")
            print("----------------")

    elif choice == "2":
        name = input("Enter contact name: ")
        number = input("Enter contact number: ")
        email = input("Enter contact email: ")

        new_contact = Contact(name, number, email)
        contacts.append(new_contact.to_dict())
        save_contacts(contacts)

        print("Contact added.")

    elif choice == "3":
        search_name = input("Enter contact name: ")

        found = False

        for contact in contacts:
            if contact["name"] == search_name:
                print(f"Name: {contact['name']}")
                print(f"Number: {contact['number']}")
                print(f"Email: {contact['email']}")
                found = True

        if not found:
            print("Contact not found.")

    elif choice == "4":
        name = input("Enter contact name to delete: ")

        for contact in contacts:
            if contact["name"] == name:
                contacts.remove(contact)
                save_contacts(contacts)
                print("Contact deleted.")
                break
        else:
            print("Contact not found.")

    elif choice == "5":
        print("Goodbye!")
        break