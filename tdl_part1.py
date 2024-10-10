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
        task_name = input("Enter the task: ")
        task_list.append(task_name)
        print(f"'{task_name}' has been added to the list.")

        continue
    
    if user_input == 2:
        # Write the Remove Task logic
        
        continue
    
    if user_input == 3:
        # Write the View Tasks logic
        
        continue
    
    if user_input == 4:
        print("Exiting the application. Goodbye!")
        break
