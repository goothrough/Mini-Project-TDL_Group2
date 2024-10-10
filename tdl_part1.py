def add_task():
    while True:
        task_name = input("Enter the task or type 1 to go back: ")
        if task_name == "1":
            break

        if task_name in task_list:
            print("This task already exists. Try again.")
        else:
            task_list.append(task_name)
            print(f"'{task_name}' has been added to the list.")
            break

def del_task():
    while True:
        remove_task = input("Enter the task to remove or type 1 to go back:")
        if remove_task == "1":
            break
        if remove_task in task_list:
            task_list.remove(remove_task)
            print(f"{remove_task} has been remove from the list")
            break
        if not remove_task in task_list:
            print(f"{remove_task} is not on the list, please try again")

def veiw_task():
    if not task_list:
        print("The list is empty, no task added yet.")

    else:
        print("To-Do List:")
        for i in range(len(task_list)):
            print(f"{i+1}. {task_list[i]}")

    print()


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
        add_task()
        continue
    
    if user_input == 2:
        del_task()
        continue
    
    if user_input == 3:
        veiw_task()
        continue
    
    if user_input == 4:
        print("Exiting the application. Goodbye!")
        break
