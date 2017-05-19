"""Task menu parts"""

import main
import projects
import users


def show_tasks(project):
    """Print task attached to given project"""
    task_list = main.get_table_from_file("tasks.csv")
    # print(task_list)
    # print(project)
    title_list = ["Name", "Project", "Info", "Owner", "Status", "Importance", "Due date"]
    tasks = [row for row in task_list if row[1] == project]
    # print(tasks)
    main.print_table(tasks, title_list)
    main.wait()


def modify_tasks_menu(active_projects):
    """Modify tasks submenu from active projects"""
    menu_items = ("Reassign task", "Change task details", "Delete task")
    cont = True
    while cont:
        option = main.menu_drawer("Modify tasks", menu_items, "Back to Current projects")
        if option == 1:
            continue
        elif option == 2:
            continue
        elif option == 3:
            continue
        else:
            cont = False
    return False


def add(project_list):
    task_list = main.get_table_from_file("tasks.csv")
    available = projects.user_projects(project_list)
    if available is False:
        return project_list
    option_list = [row[0] for row in available]
    option = main.choose_from_list(option_list)
    project_key = [row[4] for row in available if row[0] == option][0]
    name = input("Task name: ")
    desc = input("Description: ")
    due = input("Due date (as: 2016.01.01 15:00): ")
    user = users.username()
    task_list.append([name, project_key, "Not assigned", desc, "Not assigned", "Normal", due])
    print(name, "task created.")
    main.write_table_to_file("tasks.csv", task_list)
    main.wait()


def finished_all_task(project_id):
    task_list = main.get_table_from_file("tasks.csv")
    for task in task_list:
        if task[1] == project_id:
            return False
    return True


def tasks():
    """Tasks submenu"""
    menu_items = ("My tasks", "Start/automate/stop task timer", "Change task status",
                  "Add comment")
    cont = True
    while cont:
        option = main.menu_drawer("Task manager", menu_items, "Back to Projects")
        if option == 1:
            continue
        elif option == 2:
            continue
        elif option == 3:
            continue
        elif option == 4:
            continue
        else:
            cont = False
    return False
