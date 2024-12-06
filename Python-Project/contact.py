import json
import re


class ContactManager:
    """_summary_"""

    def __init__(self, file_name):
        self.file_name = file_name
        self.contacts = self.load_contacts()

    def load_contacts(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        try:
            with open(self.file_name, "r", encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_contacts(self):
        """_summary_"""
        with open(self.file_name, "w", encoding="utf-8") as file:
            json.dump(self.contacts, file)

    def display_contacts(self):
        """_summary_"""
        if self.contacts:
            for i, contact in enumerate(self.contacts, start=1):
                print(
                    f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}"
                )
        else:
            print("No contacts available")


class ContactBook(ContactManager):
    """_summary_

    Args:
        ContactManager (_type_): _description_
    """

    def __init__(self, file_name):
        """_summary_

        Args:
            file_name (_type_): _description_
        """
        super().__init__(file_name)

    def validate_email(self, email):
        """_summary_

        Args:
            email (_type_): _description_

        Returns:
            _type_: _description_
        """
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return bool(re.match(pattern, email))

    def add_contacts(self):
        """_summary_"""
        name = input("Enter contact name: ").strip()
        phone = input("Enter contact phone: ").strip()
        email = input("Enter contact email: ").strip()
        if not self.validate_email(email):
            print("Invalid email format")
            return
        self.contacts.append({"name": name, "phone": phone, "email": email})
        print("Contact added successfully!!!")
        self.save_contacts()

    def search_contacts(self):
        """_summary_"""
        if not self.contacts:
            print("No contact available")
            return
        search_contact = (
            input("Enter name or phone to search for contact: ").strip().lower()
        )
        result = [
            contact
            for contact in self.contacts
            if search_contact in contact["name"].lower()
            or search_contact in contact["phone"]
        ]
        if result:
            print("\nSearch Result: ")
            for contact in result:
                print(
                    f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}"
                )
        else:
            print("No found search!!!")

    def update_contacts(self):
        """_summary_"""
        if not self.contacts:
            print("No contact available")
            return
        update_contact = (
            input("Enter name, phone, email of contact you want to update: ")
            .strip()
            .lower()
        )
        result = [
            contact
            for contact in self.contacts
            if update_contact in contact["name"] or update_contact in contact["phone"]
        ]

        if not result:
            print("No matching contact found!!!")
            return
        if len(result) > 1:
            print("Multiple contact found!!!")
            for i, contact in enumerate(self.contacts, start=1):
                print(
                    f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}"
                )
            index = int(input("Enter the number of contact you want to update: ")) - 1
            contact_update = result[index]
        else:
            contact_update = result[0]

        print("Updating contact")
        contact_update["name"] = (
            input(f"Enter new name ({contact_update['name']}): ").strip()
            or contact_update["name"]
        )
        contact_update["phone"] = (
            input(f"Enter new name ({contact_update['phone']}): ").strip()
            or contact_update["phone"]
        )
        contact_update["email"] = (
            input(f"Enter new name ({contact_update['email']}): ")
            or contact_update["email"]
        )
        print("Contact Updated Successfully!!")
        self.save_contacts()

    def delete_contact(self):
        """_summary_"""
        if not self.contacts:
            print("No contact available")
            return
        search_term = (
            input("Enter name or phone of contact you wish to delete: ").strip().lower()
        )
        delete_terms = [
            contact
            for contact in self.contacts
            if search_term in contact["name"].lower() or search_term in contact["phone"]
        ]

        if not delete_terms:
            print("No matching terms..")
            return
        if len(delete_terms) > 1:
            print("Multiple contact found..")
            for i, contact in enumerate(self.contacts, start=1):
                print(
                    f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}"
                )
            index = int(input("Enter the number of contact you want to update: ")) - 1
            contact_delete = delete_terms[index]
        else:
            contact_delete = delete_terms[0]

        self.contacts.remove(contact_delete)
        print("Contact deleted successfully!!")
        self.save_contacts()


# Main program
if __name__ == "__main__":
    contact_book = ContactBook("contacts.json")

    while True:
        print("\nContact Book Menu:")
        print("1. View Contacts")
        print("2. Add Contact")
        print("3. Search Contacts")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice:  ").lower()

        if choice == "1":
            contact_book.display_contacts()
        elif choice == "2":
            contact_book.add_contacts()
        elif choice == "3":
            contact_book.search_contacts()
        elif choice == "4":
            contact_book.update_contacts()
        elif choice == "5":
            contact_book.delete_contact()
        elif choice == "6":
            print("Good bye")
            break
        else:
            print("Invalid choice")
