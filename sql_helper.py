import sqlite3

db_name = "./national_park.sqlite3"

def get_all(sql):
    """Gets all data from a table

    Args:
        sql (string): sql query to get all data from a table

    Returns:
        list: all dictionaries from table
    """
    with sqlite3.connect(db_name) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(sql)

        dataset = db_cursor.fetchall()

    return dataset


def get_single(sql, id):
    """Gets a single row of data from a table

    Args:
        sql (string): sql query to get a row of data from a table
        id (int): primary key of row from table
    """
    with sqlite3.connect(db_name) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(sql, ( id, ))

        data = db_cursor.fetchone()

    return data

def create_resource(sql, sql_values, new_resource):
    """Creates a new row of data

    Args:
        sql (string): sql query to insert new data into a new row.
        new_resource (string): the new data in question
    """
    with sqlite3.connect(db_name) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(sql, sql_values)

        new_resource_id = db_cursor.lastrowid
        new_resource['id'] = new_resource_id

    return new_resource

def get_all_by_param(sql, id):
    """Function that executes the SQL query with the id as a parameter and returns a filtered list of the resource by parameter."""
    with sqlite3.connect(db_name) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute(sql, (id, ))

    return db_cursor.fetchall()

def update_resource(sql, sql_values):
    """Updates a resource in SQL database. Parameters, 'sql' and 'sql_values', are used to connect to the database specified by 'db_name', executes the SQL query, and returns the number of rows affected by the query."""
    with sqlite3.connect(db_name) as conn:
        db_cursor = conn.cursor()
        db_cursor.execute(sql, sql_values)
    return db_cursor.rowcount


def delete_resource(sql, id):
    """Deletes a resource from a database using the provided SQL query and Id """
    with sqlite3.connect(db_name) as conn:
        db_cursor = conn.cursor()
        db_cursor.execute(sql, (id, ))
        