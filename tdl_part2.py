from sys import flags


def display_main_menu():
    print("Advanced To-Do List Application")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Suggest Tasks")
    print("5. Exit")

def add_task():
    #Write code here
    print()
    
def remove_task():
    #Write code here
    while True:
        rem_task = input("Enter the task to remove or type 1 to go back:")
        if rem_task == "1":
            break
        for i, task in enumerate(task_list):
            if task["task_name"] == rem_task:
                del task_list[i]
                print(f"{rem_task} has been remove from the list")
                print()
                break
        if not rem_task in task_list:
            print(f"{rem_task} is not on the list, please try again")
            continue
    print()
    print()

def view_task():
  #Write code here  
    print()   
    
def suggest_task():
    #Write code here    
    print()

task_list = [
    {"task_name": "dummy_task1", "priority": "high", "deadline": "2024-10-12"},
    {"task_name": "dummy_task2", "priority": "mid", "deadline": "2024-10-15"},
    {"task_name": "dummy_task3", "priority": "low", "deadline": "2024-10-20"},
]
# These dummy data will be removed later.


while True:
    display_main_menu()

    user_input = input("Enter your choice: ")

    if not user_input.isnumeric():
        print(f"{user_input} is not a valid input")
        print("Please try again")
        print()
        continue

    user_input = int(user_input)

    if not user_input in [1, 2, 3, 4, 5]:
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
        suggest_task()
        continue
    
    if user_input == 5:
        print("Exiting the application. Goodbye!")
        break
