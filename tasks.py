"""This module handles the task-, and project-related events.
It connects to the data_handler module if necessary and
handles the returned results.
Pass the processed data back to the main routing module.

"""

import data_handler


def get_counters(user_id):
    """Get the counts of the user's current tasks and projects

    :return: {task_count, project_count, team_count}
    """
    tasks = data_handler.user_current_task_count(user_id)[0][0]
    projects = data_handler.user_current_project_count(user_id)[0][0]
    teams = data_handler.user_current_team_count(user_id)[0][0]
    return {"task_count": tasks, "project_count": projects, "team_count": teams}


def all_tasks(user_id):
    """Get the user's ongoing tasks.

    :return: {personal_tasks, team_tasks, last_three_task}
    """
    personal_tasks = data_handler.users_all_personal_task(user_id)
    team_tasks = data_handler.users_all_teams_task(user_id)
    last_three_task = data_handler.users_last_three_task(user_id)
    return {"personal_tasks": personal_tasks, "team_tasks": team_tasks, "last_three_task": last_three_task}
