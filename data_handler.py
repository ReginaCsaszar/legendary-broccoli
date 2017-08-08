"""This module creates sql query statements, pass them to the data_manager module,
and handles the returned results or occured database errors.

"""


import psycopg2
import data_manager


def user_current_task_count(user_id):
    return data_manager.execute_select("""SELECT count(id) FROM tasks
                                        WHERE owner_id=%(user_id)s
                                        AND tasks.status != 'Done';""", {'user_id': user_id})


def user_current_team_count(user_id):
    return data_manager.execute_select("""SELECT count(id) FROM members
                                        WHERE user_id=%(user_id)s;""", {'user_id': user_id})


def user_current_project_count(user_id):
    return data_manager.execute_select("""SELECT count(id) FROM projects
                                        WHERE owner_id=%(user_id)s OR team_id=(
                                            SELECT team_id FROM members WHERE user_id=%(user_id)s)
                                        AND status != 'Done';""", {'user_id': user_id})


def users_all_personal_task(user_id):
    return data_manager.execute_select("""SELECT tasks.* FROM tasks
                                        JOIN projects ON tasks.project_id=projects.id
                                        WHERE tasks.owner_id=%(user_id)s
                                            AND tasks.status != 'Done'
                                            AND projects.team_id IS NULL;""", {'user_id': user_id})


def users_all_teams_task(user_id):
    return data_manager.execute_select("""SELECT tasks.* FROM tasks
                                        JOIN projects ON tasks.project_id=projects.id
                                        WHERE tasks.owner_id=%(user_id)s
                                            AND tasks.status != 'Done'
                                            AND projects.team_id IS NOT NULL;""", {'user_id': user_id})


def users_last_three_task(user_id):
    return data_manager.execute_select("""SELECT tasks.*
                                            FROM tasks
                                            JOIN projects ON tasks.project_id = projects.id
                                            WHERE tasks.owner_id=%(user_id)s
                                                AND tasks.status != 'Done'
                                            LIMIT 3;""", {'user_id': user_id})
