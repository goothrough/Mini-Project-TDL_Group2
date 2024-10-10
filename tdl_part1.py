task_list = []

while True:
    print("To-Do List Application")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")
    user_input = input("Enter your choice: ")
    user_input = int(user_input)

    if user_input == 1:
        # Write the Add Task logic
        
        continue
    
    if user_input == 2:
        # Write the Remove Task logic
        while True:
            remove_task = input("Enter the task to remove: ")
            if remove_task in task_list:
                task_list.remove(remove_task)
                print(f"{remove_task} has been remove from the list")
                break
            if not remove_task in task_list:
                print(f"{remove_task} is not on the list, please try again")
        continue
    
    if user_input == 3:
        # Write the View Tasks logic
        
        continue
    
    if user_input == 4:
        # Finish the program
        break
