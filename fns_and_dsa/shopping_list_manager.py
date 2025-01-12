def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item you want to add to your shopping card: ")
            shopping_list.append(item)
            pass
        elif choice == '2':
            item = input("Enter the item you want to remove from your shopping card: ")
            shopping_list.remove(item)
            pass
        elif choice == '3':
            for item in shopping_list:
                print(item)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()