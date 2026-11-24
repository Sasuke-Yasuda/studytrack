#importing task manager to connect main.py to task_manager.py
import task_manager


def show_menu():
    """Display the StudyTrack menu."""
    print("\n===== STUDYTRACK =====")
    print("1. Add homework")
    print("2. View homework")
    print("3. Update homework")
    print("4. Delete homework")
    print("5. Exit")


def main():
    """Run the StudyTrack application."""
    #keeps the application running
    while True:
        show_menu()

        choice = input("Choose an option (1-5): ")

        # Add homework
        if choice == "1":
            description = input("Enter homework description: ")

            #handles errors
            try:
                task = task_manager.add_task(description)
                print(f"Homework added! ID: {task['id']}")
            except ValueError as error:
                print(error)

        # View homework
        elif choice == "2":
            tasks = task_manager.view_tasks()

            if not tasks:
                print("You have no homework assignments.")
            else:
                print("\nYour homework assignments:")
                #goes through the each assigments and displays the description of the assignment
                for task in tasks:
                    print(f"ID: {task['id']} - {task['description']}")

        # Update homework
        elif choice == "3":
            try:
                task_id = int(input("Enter the homework ID to update: "))
                description = input("Enter the new description: ")

                task = task_manager.update_task(task_id, description)
                print(f"Homework updated! ID: {task['id']}")

            except ValueError as error:
                print(error)

        # Delete homework
        elif choice == "4":
            try:
                task_id = int(input("Enter the homework ID to delete: "))

                task = task_manager.delete_task(task_id)
                print(f"Deleted: {task['description']}")

            except ValueError as error:
                print(error)

        # Exit
        elif choice == "5":
            print("Goodbye! Good luck with your studies.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
