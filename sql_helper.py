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
