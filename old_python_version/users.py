"""Program parts for handling users"""

import main
import projects
import tasks


def username():
    """Read the current user from file"""
    with open("user.txt") as file:
        username = file.read()
    return username


def set_user():
    try:
        name = username()
    except FileNotFoundError:
        name = input("Please choose an user name: ")
        with open("user.txt", "w") as file:
            file.write(name)
    print("Welcome", name)


def other_users(project_list):
    main.print_table(project_list, ["ID", "Project name", "Owner"])
    which = main.chooser(len(project_list))
    users = main.get_table_from_file("users.csv")
    current_users = [row[1] for row in users if row[0] == which][0]
    print("Users in", project_list[which-1][1], "project: ", end="")
    [print(i, end=", ") for i in current_users]
    main.wait()
    return None


def users(task_list, project_list):
    """Users submenu"""
    iam = username()
    main_menu_items = ("Assign myself to task", "Assign myself to project", "Users in project",
                       "My active tasks", "My active projects")
    cont = True
    while cont:
        option = main.menu_drawer("User manager", main_menu_items, "Back to Projects")
        if option == 1:
            continue
        elif option == 2:
            continue
        elif option == 3:
            other_users(project_list)
        elif option == 4:
            continue
        elif option == 5:
            projects.my_active_projects(iam, project_list)
        else:
            cont = False
    return False
