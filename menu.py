"""Main parts, menu items, menu chooser, table printing"""

import os
import projects


def menu_drawer(title, menu_items, exit_title):
    """Print menu title, items and exit options, then call cooser function for ask an option\n
    return option as integer
    """
    os.system('clear')
    print(title, "\n")
    for index, item in enumerate(menu_items):
        print(index+1, item)
    print("0", exit_title, "\n")
    return chooser(len(menu_items))


def chooser(max_value):
    """Asks for a menu option.\n
    return option as integer
    """
    again = True
    while again:
        option = input("Please choose an option: ")
        try:
            option = int(option)
        except TypeError:
            print("Invalid option. Please type a number!")
        else:
            if option >= 0 and option <= max_value:
                again = False
            else:
                print("Invalid option. Please choose between 0 and", max_value)
    return option


def print_table(table, title_list):
    """print out the table"""
    # set the max lenght from table or title
    max_lenght = []
    for i in range(len(title_list)):
        max_table = max([len(ta_row[i]) for ta_row in table])
        if max_table > len(title_list[i]):
            max_lenght.append(max_table + 2)
        else:
            max_lenght.append(len(title_list[i]) + 2)
    # print table headers and title
    print("/", end="")
    for le in max_lenght:
        print("-" * le, end="--")
    print("\b\\\n|", end="")
    for lng, title in zip(max_lenght, title_list):
            print("{0:^{width}}".format(title, width=lng), "|", end="")
    print("")
    # print table content
    for row in table:
        print("|", end="")
        for lng in max_lenght:
            print("-" * lng, end="-|")
        print("\n|", end="")
        for lng, field in zip(max_lenght, row):
            print("{0:^{width}}".format(field, width=lng), "|", end="")
        print("")
    print("\\", end="")
    # print last border line
    for le in max_lenght:
        print("-" * le, end="--")
    print("\b/")
    return False


def main():
    main_menu_items = ("Start new project", "Current projects", "Tasks", "Archived projects", "Users")
    cont = True
    while cont:
        option = menu_drawer("Project manager", main_menu_items, "Exit")
        if option == 1:
            continue
        elif option == 2:
            projects.active_projects()
        elif option == 3:
            continue
        elif option == 4:
            projects.archived_projects()
        elif option == 5:
            continue
        else:
            cont = False
    return False

if __name__ == '__main__':
    main()
