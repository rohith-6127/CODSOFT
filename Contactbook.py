import json
import os
import re

# =====================================================
# ADVANCED CONTACT MANAGEMENT SYSTEM
# =====================================================

FILE_NAME = "contacts.json"

# ANSI Colors
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
RESET = "\033[0m"


# =====================================================
# FILE HANDLING
# =====================================================

def load_contacts():
    """Load contacts from JSON file."""
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except:
            return []
    return []


def save_contacts():
    """Save contacts to JSON file."""
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


contacts = load_contacts()


# =====================================================
# VALIDATION FUNCTIONS
# =====================================================

def validate_phone(phone):
    """Validate phone number."""
    return phone.isdigit() and len(phone) >= 7


def validate_email(email):
    """Validate email address."""
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email)


def phone_exists(phone, ignore_index=None):
    """Check for duplicate phone number."""
    for index, contact in enumerate(contacts):
        if contact["phone"] == phone and index != ignore_index:
            return True
    return False


# =====================================================
# DISPLAY FUNCTIONS
# =====================================================

def display_contact(contact, index=None):

    print("\n" + "-" * 50)

    if index is not None:
        print(f"Contact ID : {index}")

    print(f"Name       : {contact['name']}")
    print(f"Phone      : {contact['phone']}")
    print(f"Email      : {contact['email']}")
    print(f"Address    : {contact['address']}")
    print(f"Category   : {contact['category']}")

    if contact["favorite"]:
        print(f"Favorite   : ⭐ Yes")
    else:
        print(f"Favorite   : No")

    print("-" * 50)


# =====================================================
# ADD CONTACT
# =====================================================

def add_contact():

    print(CYAN + "\n========== ADD NEW CONTACT ==========" + RESET)

    name = input("Enter Name: ").strip()

    while True:
        phone = input("Enter Phone Number: ").strip()

        if not validate_phone(phone):
            print(RED + "Invalid phone number!" + RESET)
        elif phone_exists(phone):
            print(RED + "This phone number already exists!" + RESET)
        else:
            break

    while True:
        email = input("Enter Email: ").strip()

        if validate_email(email):
            break

        print(RED + "Invalid email format!" + RESET)

    address = input("Enter Address: ").strip()

    category = input(
        "Enter Category (Family/Friends/Work/Other): "
    ).strip().capitalize()

    favorite_input = input("Mark as Favorite? (y/n): ").lower()

    favorite = favorite_input == "y"

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address,
        "category": category,
        "favorite": favorite
    }

    contacts.append(contact)

    save_contacts()

    print(GREEN + "\nContact Added Successfully! ✅" + RESET)


# =====================================================
# VIEW CONTACTS
# =====================================================

def view_contacts():

    if not contacts:
        print(RED + "\nNo contacts available!" + RESET)
        return

    print(CYAN + "\n========== CONTACT LIST ==========" + RESET)

    sorted_contacts = sorted(
        contacts,
        key=lambda x: (not x["favorite"], x["name"].lower())
    )

    for index, contact in enumerate(sorted_contacts, start=1):

        star = "⭐" if contact["favorite"] else ""

        print(
            f"{index}. {star} "
            f"{contact['name']} | "
            f"{contact['phone']} | "
            f"{contact['category']}"
        )


# =====================================================
# SEARCH CONTACT
# =====================================================

def search_contact():

    keyword = input(
        "\nEnter Name or Phone Number to Search: "
    ).lower()

    found = False

    for index, contact in enumerate(contacts, start=1):

        if (
            keyword in contact["name"].lower()
            or keyword in contact["phone"]
        ):

            display_contact(contact, index)
            found = True

    if not found:
        print(RED + "\nNo Matching Contact Found!" + RESET)


# =====================================================
# UPDATE CONTACT
# =====================================================

def update_contact():

    view_contacts()

    if not contacts:
        return

    try:
        index = int(
            input("\nEnter Contact ID to Update: ")
        ) - 1

        if index < 0 or index >= len(contacts):
            print(RED + "Invalid Contact ID!" + RESET)
            return

        contact = contacts[index]

        print(
            "\nPress ENTER to keep the existing value."
        )

        new_name = input(
            f"Name [{contact['name']}]: "
        ).strip()

        new_phone = input(
            f"Phone [{contact['phone']}]: "
        ).strip()

        new_email = input(
            f"Email [{contact['email']}]: "
        ).strip()

        new_address = input(
            f"Address [{contact['address']}]: "
        ).strip()

        new_category = input(
            f"Category [{contact['category']}]: "
        ).strip()

        if new_name:
            contact["name"] = new_name

        if new_phone:

            if not validate_phone(new_phone):
                print(RED + "Invalid phone number!" + RESET)
                return

            if phone_exists(new_phone, index):
                print(RED + "Phone number already exists!" + RESET)
                return

            contact["phone"] = new_phone

        if new_email:

            if not validate_email(new_email):
                print(RED + "Invalid email format!" + RESET)
                return

            contact["email"] = new_email

        if new_address:
            contact["address"] = new_address

        if new_category:
            contact["category"] = new_category.capitalize()

        favorite = input(
            "Change Favorite Status? (y/n/skip): "
        ).lower()

        if favorite == "y":
            contact["favorite"] = True

        elif favorite == "n":
            contact["favorite"] = False

        save_contacts()

        print(
            GREEN +
            "\nContact Updated Successfully! ✅" +
            RESET
        )

    except ValueError:

        print(
            RED +
            "Please enter a valid number!" +
            RESET
        )


# =====================================================
# DELETE CONTACT
# =====================================================

def delete_contact():

    view_contacts()

    if not contacts:
        return

    try:

        index = int(
            input("\nEnter Contact ID to Delete: ")
        ) - 1

        if index < 0 or index >= len(contacts):
            print(RED + "Invalid Contact ID!" + RESET)
            return

        contact = contacts[index]

        confirm = input(
            f"Delete {contact['name']}? (y/n): "
        ).lower()

        if confirm == "y":

            contacts.pop(index)

            save_contacts()

            print(
                GREEN +
                "\nContact Deleted Successfully! 🗑️" +
                RESET
            )

        else:

            print(
                YELLOW +
                "Deletion Cancelled." +
                RESET
            )

    except ValueError:

        print(
            RED +
            "Invalid Input!" +
            RESET
        )


# =====================================================
# FAVORITE CONTACTS
# =====================================================

def show_favorites():

    favorites = [
        contact
        for contact in contacts
        if contact["favorite"]
    ]

    if not favorites:

        print(
            YELLOW +
            "\nNo Favorite Contacts Found!" +
            RESET
        )

        return

    print(
        MAGENTA +
        "\n========== ⭐ FAVORITE CONTACTS ==========" +
        RESET
    )

    for index, contact in enumerate(favorites, start=1):

        print(
            f"{index}. "
            f"{contact['name']} | "
            f"{contact['phone']}"
        )


# =====================================================
# CATEGORY SEARCH
# =====================================================

def search_by_category():

    category = input(
        "\nEnter Category: "
    ).strip().lower()

    found = False

    for index, contact in enumerate(contacts, start=1):

        if contact["category"].lower() == category:

            display_contact(contact, index)

            found = True

    if not found:

        print(
            RED +
            "\nNo Contacts Found in This Category!" +
            RESET
        )


# =====================================================
# STATISTICS
# =====================================================

def show_statistics():

    total = len(contacts)

    favorites = len([
        c for c in contacts
        if c["favorite"]
    ])

    categories = {}

    for contact in contacts:

        category = contact["category"]

        categories[category] = categories.get(
            category,
            0
        ) + 1

    print(
        BLUE +
        "\n========== CONTACT STATISTICS ==========" +
        RESET
    )

    print(f"Total Contacts     : {total}")
    print(f"Favorite Contacts  : {favorites}")

    print("\nContacts by Category:")

    if categories:

        for category, count in categories.items():

            print(
                f"  {category}: {count}"
            )

    else:

        print("No category data available.")


# =====================================================
# MAIN MENU
# =====================================================

while True:

    print(CYAN)

    print("\n" + "=" * 55)

    print(
        "        📱 ADVANCED CONTACT MANAGEMENT SYSTEM"
    )

    print("=" * 55)

    print(RESET)

    print("1.  Add Contact")
    print("2.  View Contact List")
    print("3.  Search Contact")
    print("4.  Update Contact")
    print("5.  Delete Contact")
    print("6.  View Favorite Contacts ⭐")
    print("7.  Search by Category")
    print("8.  Contact Statistics")
    print("9.  Exit")

    choice = input(
        "\nEnter Your Choice: "
    )

    if choice == "1":

        add_contact()

    elif choice == "2":

        view_contacts()

    elif choice == "3":

        search_contact()

    elif choice == "4":

        update_contact()

    elif choice == "5":

        delete_contact()

    elif choice == "6":

        show_favorites()

    elif choice == "7":

        search_by_category()

    elif choice == "8":

        show_statistics()

    elif choice == "9":

        save_contacts()

        print(
            GREEN +
            "\nThank you for using Contact Management System! 👋" +
            RESET
        )

        break

    else:

        print(
            RED +
            "\nInvalid Choice! Please try again." +
            RESET
        )
