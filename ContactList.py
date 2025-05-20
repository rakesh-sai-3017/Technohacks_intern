def main():
    contacts = {}
    
    print("Welcome to Simple Contact Book!")
    print("Commands: add, search, delete, list, exit")
    
    while True:
        command = input("\nEnter command: ").strip().lower()
        
        if command == "exit":
            print("Goodbye!")
            break
            
        elif command == "add":
            name = input("Enter contact name: ").strip()
            if not name:
                print("Name cannot be empty!")
                continue
                
            phone = input("Enter phone number: ").strip()
            if not phone:
                print("Phone number cannot be empty!")
                continue
                
            contacts[name] = phone
            print(f"Contact '{name}' added successfully!")
            
        elif command == "search":
            name = input("Enter name to search: ").strip()
            if name in contacts:
                print(f"Name: {name}, Phone: {contacts[name]}")
            else:
                print(f"Contact '{name}' not found.")
                
        elif command == "delete":
            name = input("Enter name to delete: ").strip()
            if name in contacts:
                del contacts[name]
                print(f"Contact '{name}' deleted successfully!")
            else:
                print(f"Contact '{name}' not found.")
                
        elif command == "list":
            if not contacts:
                print("No contacts in the book.")
            else:
                print("\nContact List:")
                for name, phone in contacts.items():
                    print(f"{name}: {phone}")
                    
        else:
            print("Invalid command. Please try again.")
            print("Available commands: add, search, delete, list, exit")

if __name__ == "__main__":
    main()
