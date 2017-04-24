"""Program parts for projects"""

import menu


def archived_projects():
    """Archived projects handler menu"""
    title = "Archived projects"
    menu_items = ("List all archived projects", "Search in archives", "Show project details", "Show project statistics")
    cont = True
    while cont:
        option = menu.menu_drawer(title, menu_items, "Back to Projects")
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


def active_projects():
    """Archive projects handler menu"""
    title = "Active projects"
    menu_items = ("Add new project", "Delete project", "Show project details", "Show project statistic")
    cont = True
    while cont:
        option = menu.menu_drawer(title, menu_items, "Back to Projects")
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