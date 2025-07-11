from datetime import datetime

todo_list = []

def add_task():
    task = input("Enter the task: ")
    priority = input("Priority (High/Medium/Low): ").capitalize()
    due_date = input("Due date (YYYY-MM-DD) or leave blank: ")

    if due_date:
        try:
            due_date_obj = datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Skipping due date.")
            due_date_obj = None
    else:
        due_date_obj = None

    todo_list.append({
        "task": task,
        "priority": priority,
        "due_date": due_date_obj
    })
    print("Task added successfully.")

def view_tasks():
    if not todo_list:
        print("No tasks to show.")
        return

    sort_choice = input("Sort by priority or date? (priority/date/none): ").lower()

    if sort_choice == "priority":
        priority_order = {"High": 1, "Medium": 2, "Low": 3}
        sorted_list = sorted(todo_list, key=lambda x: priority_order.get(x["priority"], 4))
    elif sort_choice == "date":
        sorted_list = sorted(todo_list, key=lambda x: x["due_date"] or datetime.max)
    else:
        sorted_list = todo_list

    print("\n--- To-Do List ---")
    for idx, item in enumerate(sorted_list, start=1):
        due = item["due_date"].strftime("%Y-%m-%d") if item["due_date"] else "No due date"
        print(f"{idx}. {item['task']} | Priority: {item['priority']} | Due: {due}")

def delete_task():
    view_tasks()
    try:
        task_no = int(input("Enter task number to delete: "))
        if 1 <= task_no <= len(todo_list):
            del todo_list[task_no - 1]
            print("Task deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    print("\n--- To-Do List App ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Try again.")
