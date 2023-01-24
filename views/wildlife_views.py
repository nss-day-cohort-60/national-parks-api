import sqlite3
from models import Wildlife
from sql_helper import get_all, get_single


def get_all_wildlife():
    """Function to retrieve all wildlife from a database and return the data as a list of dictionaries"""
    sql = """
            SELECT 
            w.id,
            w.name,
            w.information,
            w.wildlife_group_id,
            w.image
            FROM wildlife w
            """

    all_wildlife = []
    
    dataset = get_all(sql)

    for row in dataset:
        wildlife = Wildlife(row['id'], row['name'], row['information'],
                            row['wildlife_group_id'], row['image'])

        all_wildlife.append(wildlife.__dict__)

    return all_wildlife


def get_single_wildlife_type(id):
    """A function that retrieves a single wildlife type based on the given id"""
    sql = """
            SELECT 
            w.id,
            w.name,
            w.information,
            w.wildlife_group_id,
            w.image
            FROM wildlife w
            WHERE w.id = ?
            """

    data = get_single(sql, id)
    
    if not data:
        return {}

    wildlife = Wildlife(data['id'], data['name'], data['information'],
                        data['wildlife_group_id'], data['image'])

    return wildlife.__dict__


def get_wildlife_by_park_id(park_id):
    """A function that takes in one parameter and used to retrieve information about wildlife in a specific park."""
    with sqlite3.connect("./national_park.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
        w.id,
        w.name,
		w.information,
		w.wildlife_group_id,
		w.image
        FROM Park_Wildlife pw
        JOIN Wildlife w
            ON pw.wildlife_id = w.id
        WHERE pw.park_id = ?
		ORDER BY w.name ASC;
        """, (park_id, ))

        all_wildlife = []

        dataset = db_cursor.fetchall()

        if not dataset:
            return []

        if len(dataset) > 0:
            for row in dataset:
                wildlife = Wildlife(row['id'], row['name'], row['information'],
                                    row['wildlife_group_id'], row['image'])

                result = wildlife.__dict__
                all_wildlife.append(result)

    return all_wildlife

def create_wildlife(new_wildlife):
    with sqlite3.connect("./national_park.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Wildlife
            ( name, information, wildlife_group_id, image)
        VALUES
            ( ?, ?, ?, ?);
        """, (new_wildlife['name'], new_wildlife['information'],
              new_wildlife['wildlife_group_id'], new_wildlife['image']))

        id = db_cursor.lastrowid

        # Add the `id` property to the wildlife dictionary
        new_wildlife['id'] = id

    return new_wildlife


def update_wildlife(id, new_order):
    """iterates the list of wildlife until it finds the right one, and then replaces it with what the client sent as the replacement."""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Orders
            SET
                metal_id = ?,
                size_id = ?,
                style_id = ?,
                timestamp = ?
        WHERE id = ?
        """, (new_order['metal_id'], new_order['size_id'],
              new_order['style_id'], new_order['timestamp'], id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
        # Forces 204 response by main module
    return True
