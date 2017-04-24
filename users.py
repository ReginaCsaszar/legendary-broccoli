"""Program parts for handling users"""

import menu


def username():
    """Read the current user from file"""
    return "Regina"


def users():
    """Users submenu"""
    main_menu_items = ("Assign myself to project", "Other users in project", "My tasks", "My projects")
    cont = True
    while cont:
        option = menu.menu_drawer("User manager", main_menu_items, "Back to Projects")
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
