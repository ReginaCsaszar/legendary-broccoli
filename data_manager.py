"""This module is dedicated to establish connection to the potgresql database, and execute sql query statements.

:select: execute_select(statement, variables=None)\n
:data manipulation: execute_dml_statement(statement, variables=None)

"""
import psycopg2
import dbconn


def establish_connection():
    """
    Create a database connection

    :returns: psycopg2.connection
    """
    connection_data = dbconn.get_connection_data()
    try:
        connect_str = "dbname={} user={} host={} password={}".format(connection_data['dbname'],
                                                                     connection_data['user'],
                                                                     connection_data['host'],
                                                                     connection_data['password'])
        conn = psycopg2.connect(connect_str)
        conn.autocommit = True
    except psycopg2.DatabaseError as e:
        print("Cannot connect to database.")
        print(e)
    else:
        return conn


def execute_select(statement, variables=None):
    """
    Execute SELECT statement optionally parameterized

    Example:
    > execute_select('SELECT %(title)s;', variables={'title': 'Codecool'})

    :statment: SELECT statement

    :variables:  optional parameter dict"""
    result_set = []
    with establish_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(statement, variables)
            result_set = cursor.fetchall()
    return result_set


def execute_dml_statement(statement, variables=None):
    """
    Execute data manipulation query statement (optionally parameterized)

    :statment: SQL statement

    :variables:  optional parameter dict"""
    with establish_connection() as conn:
        with conn.cursor() as cursor:
            result = cursor.execute(statement, variables)
