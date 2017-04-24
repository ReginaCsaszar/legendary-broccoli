"""Program parts for projects"""

import menu
import users


def project_read():
    """Read projects from file"""
    project_list = [["Personal project", "Regina", "active"],
                    ["Lightweight ERP project", "Peter", "closed"],
                    ["Tic Tac Toe game", "Tamás", "closed"],
                    ["Scratch game", "Regina", "closed"]
                    ]
    return project_list


def start_projects(project_list):
    """Start new projects"""
    again = True
    user = users.username()
    while again:
        name = input("Type new project name: ")
        project_list.append([name, user, "active"])
        again = False
    print("Project", name, "created.")
    back = input("Press enter to continue")
    return project_list


def archived_projects(project_list):
    """Archived projects handler menu"""
    archived = [row for row in project_list if row[2] == "closed"]
    title = "Archived projects"
    menu_items = ("List all archived projects", "Search in archives", "Show project details", "Show project statistics")
    cont = True
    while cont:
        option = menu.menu_drawer(title, menu_items, "Back to Projects")
        if option == 1:
            menu.print_table(archived, ["Project name", "Owner"])
            back = input("\nPress enter to continue ")
        elif option == 2:
            continue
        elif option == 3:
            continue
        elif option == 4:
            continue
        else:
            cont = False
    return False


def active_projects(project_list):
    """Archive projects handler menu"""
    archived = [row for row in project_list if row[2] is "active"]
    title = "Active projects"
    menu_items = ("Show projects", "Delete project", "Show project details", "Show project statistic")
    cont = True
    while cont:
        option = menu.menu_drawer(title, menu_items, "Back to Projects")
        if option == 1:
            menu.print_table(archived, ["Project name", "Owner"])
            back = input("\nPress enter to continue ")
        elif option == 2:
            continue
        elif option == 3:
            continue
        elif option == 4:
            continue
        else:
            cont = False
    return False
