from datetime import datetime


def display_main_menu():
    print("Advanced To-Do List Application")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Suggest Tasks")
    print("5. Exit")


def add_task():
    while True:
        task_name = input("Enter the task or type 1 to go back: ")

        if task_name == "1":
            break

        # Check for duplicate task names
        if task_name in [task.get("task_name") for task in task_list]:
            print(f"'{task_name}' already exists")
            print("Please try again")
            print()
            continue

        priority = input(
            "Enter the priority (high, medium, low) or type 1 to go back: "
        )

        if priority == "1":
            break

        # Check if the priority value is defined
        if not priority in ["high", "medium", "low"]:
            print(f"'{priority}' is not a valid priority")
            print("Please try again")
            print()
            continue

        deadline = input("Enter the deadline (YYYY-MM-DD) or type 1 to go back: ")

        if deadline == "1":
            break

        # Check the date format
        try:
            datetime.strptime(deadline, "%Y-%m-%d")
        except ValueError:
            print(f"'{deadline}' is not a valid format (YYYY-MM-DD)")
            print("Please try again")
            print()
            continue

        # Add the task to the task list
        task = {"task_name": task_name, "priority": priority, "deadline": deadline}
        task_list.append(task)

        print(
            f"'{task_name}' with priority '{priority}' and deadline '{deadline}' has been added to the list."
        )
        print()

        break


def remove_task():
    not_on_list = 0
    while True:
        rem_task = input("Enter the task to remove or type 1 to go back:")
        if rem_task == "1":
            break
        for i, task in enumerate(task_list):
            if task["task_name"] == rem_task:
                del task_list[i]
                not_on_list = 0
                print(f"{rem_task} has been remove from the list")
                print()
                break
            if not rem_task in task_list:
                not_on_list = 1
        if not_on_list == 1:
            print(f"{rem_task} is not on the list, please try again")
            print()
        continue_deleting = input(
            "What do you want to do: continue deleting task(1) or exit(any other key): "
        )
        if continue_deleting == "1":
            continue
        else:
            break
    print()


def view_task():
    while True:
        if not task_list:
            print("The list is empty, no task added yet.")

        else:
            print("To-Do List:")
            print(
                "{:<2} {:<25} {:<15} {:<10}".format("#", "Task", "Priority", "Deadline")
            )
            print("-" * 60)

            for i in range(len(task_list)):
                # print(f"{k + 1}.", task_list[k].values())
                print(
                    "{:<2} {:<25} {:<15} {:<10}".format(
                        i + 1,
                        task_list[i]["task_name"],
                        task_list[i]["priority"],
                        task_list[i]["deadline"],
                    )
                )

            print()
        break


def urgency_score(self, priority_to_priority_score):
    # Calculate urgency score (higher score = more urgent)
    # Combine deadline proximity and priority into a single score

    deadline_str = self["deadline"]
    date_deadlime = datetime.strptime(deadline_str, "%Y-%m-%d")

    days_left = (date_deadlime - datetime.now()).days

    if days_left <= 0:
        days_left = 1  # Prevent division by zero or negative days

    return priority_to_priority_score[self["priority"]] / days_left


def suggest_task():
    print()

    if len(task_list) == 0:
        print("There is no task to work on.")
        print()
        return

    # Sort the task list by urgency score, then by priority, then by deadline

    priority_to_priority_score = {"high": 3, "medium": 2, "low": 1}
    sorted_task_list = sorted(
        task_list,
        key=lambda task: (
            -urgency_score(task, priority_to_priority_score),
            -priority_to_priority_score[task["priority"]],
            datetime.strptime(task["deadline"], "%Y-%m-%d"),
        ),
    )

    print("Hello! Here are some tasks you might want to work on:")
    for task in sorted_task_list:
        print(f"{task['task_name']} - {task['priority']} - {task['deadline']}")

    print()


task_list = []


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
