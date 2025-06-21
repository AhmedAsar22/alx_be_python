def display_menu():
    """Displays the main menu to the user."""
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """Main function to run the shopping list application."""
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"'{item}' was added to the list.")

        elif choice == '2':
            # Prompt for and remove an item
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' was removed from the list.")
            else:
                print(f"'{item}' not found in the list.")

        elif choice == '3':
            # Display the shopping list
            print("\n--- Your Shopping List ---")
            if not shopping_list:
                print("The list is currently empty.")
            else:
                for index, item in enumerate(shopping_list, start=1):
                    print(f"{index}. {item}")
            print("------------------------")


        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()