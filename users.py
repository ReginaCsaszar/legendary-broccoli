"""Program parts for handling users"""

import menu
import projects
import tasks


def username():
    """Read the current user from file"""
    return "Regina"


def get_users():
    """Read all users from a file"""
    users = [[1, ["Regina"]],
             [2, ["Regina", "Péter", "Annamari", "Gergő"]],
             [3, ["Regina", "Zsófi", "Tamás"]],
             [4, ["Regina", "Ákos", "Gergő"]]
             ]
    return users


def other_users(project_list):
    menu.print_table(project_list, ["ID", "Project name", "Owner"])
    which = menu.chooser(len(project_list))
    users = get_users()
    current_users = [row[1] for row in users if row[0] == which][0]
    print("Users in", project_list[which-1][1], "project: ", end="")
    [print(i, end=", ") for i in current_users]
    menu.wait()
    return None


def users(task_list, project_list):
    """Users submenu"""
    main_menu_items = ("Assign myself to task", "Assign myself to projects", "Other users in project", "My active tasks", "My active projects")
    cont = True
    while cont:
        option = menu.menu_drawer("User manager", main_menu_items, "Back to Projects")
        if option == 1:
            continue
        elif option == 2:
            continue
        elif option == 3:
            other_users(project_list)
        elif option == 4:
            continue
        elif option == 5:
            continue
        else:
            cont = False
    return False
