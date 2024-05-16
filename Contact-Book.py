class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, address):
        self.contacts[name] = Contact(name, phone, email, address)

    def view_contacts(self):
        for name, contact in self.contacts.items():
            print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}, Address: {contact.address}")

    def search_contact(self, query):
        for name, contact in self.contacts.items():
            if query in name or query in contact.phone:
                print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}, Address: {contact.address}")

    def update_contact(self, name, phone, email, address):
        if name in self.contacts:
            self.contacts[name] = Contact(name, phone, email, address)
        else:
            print("Contact not found")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
        else:
            print("Contact not found")

if __name__ == "__main__":
    cm = ContactManager()

    while True:
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            cm.add_contact(name, phone, email, address)

        elif choice == 2:
            cm.view_contacts()

        elif choice == 3:
            query = input("Enter search query: ")
            cm.search_contact(query)

        elif choice == 4:
            name = input("Enter name: ")
            phone = input("Enter new phone: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            cm.update_contact(name, phone, email, address)

        elif choice == 5:
            name = input("Enter name: ")
            cm.delete_contact(name)

        elif choice == 6:
            break

        else:
            print("Invalid choice")