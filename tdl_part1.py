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
        
        continue
    
    if user_input == 3:
        # Write the View Tasks logic
        if not task_list:
            print("The list is empty, no task added yet.")

        else:
            print("To-Do List:")
            for i in range(len(task_list)):
                print(f"{i+1}. {task_list[i]}")

        print()

        continue
    
    if user_input == 4:
        # Finish the program
        break
