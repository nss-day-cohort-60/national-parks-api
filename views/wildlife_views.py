import sqlite3
from models import Wildlife


def get_all_wildlife():
    """Function to retrieve all wildlife from a database and return the data as a list of dictionaries"""
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
        FROM wildlife w
        """)

        all_wildlife = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            wildlife = Wildlife(row['id'], row['name'], row['information'],
                                row['wildlife_group_id'], row['image'])

            all_wildlife.append(wildlife.__dict__)

    return all_wildlife


def get_single_wildlife_type(id):
    """A function that retrieves a single wildlife type based on the given id"""
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
        FROM wildlife w
        WHERE w.id = ?
        """, (id, ))

        data = db_cursor.fetchone()
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
