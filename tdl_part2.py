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
