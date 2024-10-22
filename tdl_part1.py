def add_task():
    while True:
        task_name = input("Enter the task or type 1 to go back: ")
        if task_name == "1":
            break
        
        if task_name is None or task_name == "":
            print("Task name is required. Try again.")
            print()
            break

        if task_name in task_list:
            print("This task already exists. Try again.")
            print()
        else:
            task_list.append(task_name)
            print(f"'{task_name}' has been added to the list.")
            print()
            break
        print()

def remove_task():
    while True:
        rem_task = input("Enter the task to remove or type 1 to go back:")
        if rem_task == "1":
            break
        if rem_task in task_list:
            task_list.remove(rem_task)
            print(f"{rem_task} has been remove from the list")
            print()
            break
        if not rem_task in task_list:
            print(f"{rem_task} is not on the list, please try again")

        print()

def view_task():
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
    if not user_input.isnumeric():
        print(f"{user_input} is not a valid input")
        print("Please try again")
        print()
        continue

    user_input = int(user_input)
    
    if not user_input in [1,2,3,4]:
        print(f"{user_input} is not a valid number")
        print("Please try again")
        print()
        continue

    if user_input == 1:
        add_task()
        continue
    
    if user_input == 2:
        remove_task()
        continue
    
    if user_input == 3:
        view_task()
        continue
    
    if user_input == 4:
        print("Exiting the application. Goodbye!")
        break
