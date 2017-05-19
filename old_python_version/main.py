"""Main parts, menu items, menu chooser, table printing"""

import os
import random

import projects
import users
import tasks


def wait():
    back = input("\nPress enter to continue ")
    return None


def get_table_from_file(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
    table = [element.replace("\n", "").split(",") for element in lines]
    return table


def write_table_to_file(file_name, table):
    with open(file_name, "w") as file:
        for record in table:
            row = ','.join(record)
            file.write(row + "\n")


def generate_random():
    generated = ''
    big_tuple = ("QWERTZUIOPASDFGHJKLYXCVBNM", "qwertzuiopasdfghjklyxcvbnm", "0123456789")
    for i in range(3):
        generated += random.choice(big_tuple[i])
        generated += random.choice(big_tuple[i])
    generated += random.choice(big_tuple[1])
    generated = "".join(random.sample(generated, len(generated)))
    return generated


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


def choose_from_list(option_list):
    """Asks for an option from a list.\n
    return option as string
    """
    again = True
    while again:
        option = input("Please choose an option: ")
        try:
            option_int = int(option)
        except ValueError:
            print("Invalid option. Please type a number!")
        else:
            if option in option_list:
                again = False
            else:
                print("Invalid option. Please select one from above.")
    return option


def chooser(max_value):
    """Asks for a menu option.\n
    return option as integer
    """
    again = True
    while again:
        option = input("Please choose an option: ")
        try:
            option = int(option)
        except ValueError:
            print("Invalid option. Please type a number!")
        else:
            if option >= 0 and option <= max_value:
                again = False
            else:
                print("Invalid option. Please choose between 0 and", max_value)
    return option


def print_table(table, title_list):
    """Print out the table"""
    os.system('clear')
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
    """Print main menu and start program"""
    os.system('clear')
    users.set_user()
    wait()
    project_list = get_table_from_file("projects.csv")
    task_list = get_table_from_file("tasks.csv")
    main_menu_items = ("Start new project", "Current projects", "Tasks", "Users", "Archived projects")
    cont = True
    while cont:
        option = menu_drawer("Project manager", main_menu_items, "Exit")
        if option == 1:
            project_list = projects.start_projects(project_list)
            wait()
        elif option == 2:
            projects.active_projects(project_list)
        elif option == 3:
            tasks.tasks()
            continue
        elif option == 4:
            users.users(task_list, project_list)
        elif option == 5:
            projects.archived_projects(project_list)
        else:
            cont = False
    return False

if __name__ == '__main__':
    pass
