"""Task menu parts"""

import menu


def modify_tasks():
    """Modify tasks submenu"""
    menu_items = ("Reassign task", "Change task details", "Delete task")
    cont = True
    while cont:
        option = menu.menu_drawer("Modify task", menu_items, "Back to Task manager")
        if option == 1:
            continue
        elif option == 2:
            continue
        elif option == 3:
            continue
        else:
            cont = False
    return False


def tasks():
    """Tasks submenu"""
    menu_items = ("My tasks", "Start/stop task timer", "Change task status",
                  "Add comment", "Modify tasks")
    cont = True
    while cont:
        option = menu.menu_drawer("Task manager", menu_items, "Back to Projects")
        if option == 1:
            continue
        elif option == 2:
            continue
        elif option == 3:
            continue
        elif option == 4:
            continue
        elif option == 5:
            modify_tasks()
        else:
            cont = False
    return False
