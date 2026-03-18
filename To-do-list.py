tasks = []

while True:
    choice = input("Enter your action (add/view/update/delete/exit): ")

    if choice == 'add':
        task = input("Enter your task: ")
        tasks.append(task)

    elif choice == 'view':
        if not tasks:
            print("No tasks yet")
        else:
            for index, task in enumerate(tasks, start=1):
                print(index, task)

    elif choice == 'update':
        for index, task in enumerate(tasks, start=1):
            print(index, task)

        task_no = int(input("Enter task number to update: "))
        new_task = input("Enter new task: ")
        tasks[task_no - 1] = new_task

    elif choice == 'delete':
        for index, task in enumerate(tasks, start=1):
            print(index, task)

        task_no = int(input("Enter task number to delete: "))
        tasks.pop(task_no - 1)

    elif choice == 'exit':
        print("Exiting...")
        break

    else:
        print("Invalid choice")