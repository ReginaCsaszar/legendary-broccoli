"""Program parts for projects"""

import main
import users
import tasks


def start_projects(project_list):
    """Start new projects"""
    idn = str(len(project_list)+1)
    again = True
    user = users.username()
    serial = main.generate_random()
    name = input("Type new project name: ")
    project_list.append([idn, name, user, "active"])
    print("Project", name, "created.")
    return project_list


def user_projects(projects):
    user = users.username()
    own_list = [row for row in projects if row[2] == user]
    if own_list:
        main.print_table(own_list, ["ID", "Project name", "Owner"])
        return own_list
    else:
        print("No don't have any project!")
        return []


def my_active_projects(user, project_list):
    own_list = [row for row in project_list if row[2] == user and row[3] == "active"]
    main.print_table(own_list, ["ID", "Project name"])
    main.wait()


def close_project(filtered_list, project_list):
    own_list = user_projects(filtered_list)
    if own_list:
        option_list = [row[0] for row in own_list]
        option = main.choose_from_list(option_list)
        for row in project_list:
            if row[0] == option:
                if tasks.finished_all_task(row[4]):
                    print(row[1], " closed.")
                    row[3] = "closed"
                else:
                    print("Delete not possible. Project has unfinished tasks.")
    return project_list


def delete_project(filtered_list, project_list):
    "Delete a project"
    own_list = user_projects(filtered_list)
    if own_list:
        option_list = [row[0] for row in own_list]
    else:
        main.wait()
        return project_list
    option = main.choose_from_list(option_list)
    actual = [row for row in project_list if row[0] == option][0]
    print(actual[1], " deleted.")
    project_list.remove(actual)
    for index, row in enumerate(project_list):
        row[0] = str(index)
    main.wait()
    return project_list


def show_details(project_list):
    main.print_table(project_list, ["ID", "Project name", "Owner"])
    option = main.choose_from_list([row[0] for row in project_list])
    project = [row[4] for row in project_list if row[0] == option][0]
    tasks.show_tasks(project)


def archived_projects(project_list):
    """Archived projects handler menu"""
    title = "Archived projects"
    menu_items = ("List all archived projects", "Delete project", "Show project details", "Show project statistics")
    cont = True
    while cont:
        archived = [row for row in project_list if row[3] == "closed"]
        option = main.menu_drawer(title, menu_items, "Back to Projects")
        if option == 1:
            main.print_table(archived, ["ID", "Project name", "Owner"])
            main.wait()
        elif option == 2:
            project_list = delete_project(archived, project_list)
        elif option == 3:
            continue
        elif option == 4:
            continue
        else:
            cont = False
    return False


def active_projects(project_list):
    """Archive projects handler menu"""
    title = "Active projects"
    menu_items = ("Show projects", "Add new task", "Modify tasks",
                  "Finish project", "Show project details", "Show project statistic")
    cont = True
    while cont:
        active = [row for row in project_list if row[3] == "active"]
        option = main.menu_drawer(title, menu_items, "Back to Projects")
        if option == 1:
            if active:
                main.print_table(active, ["ID", "Project name", "Owner"])
            else:
                print("No active projects.")
            main.wait()
        elif option == 2:
            tasks.add(active)
        elif option == 3:
            tasks.modify_tasks_menu(active)
        elif option == 4:
            project_list = close_project(active, project_list)
        elif option == 5:
            show_details(active)
        elif option == 6:
            continue
        else:
            cont = False
    return False
