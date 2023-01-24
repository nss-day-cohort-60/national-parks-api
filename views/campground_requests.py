import sqlite3
from models import Campground

def get_all_campgrounds():
    """Gets all campgrounds
    Returns:
        list: All campground dictionaries"""
    with sqlite3.connect("./national_park.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id,
            c.name,
            c.park_id,
            c.available_sites,
            c.description
        FROM Campground c
        """)

        campgrounds = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            campground = Campground(row['id'], row['name'], row['park_id'], row['available_sites'], row['description'])

            campgrounds.append(campground.__dict__)

    return campgrounds

def get_single_campground(id):
    """Finds the matching campground dictionary for the specified campground id

    Args:
        id (int): campground id

    Returns:
        dict: campground dictionary
    """
    with sqlite3.connect("./national_park.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id,
            c.start_date,
            c.end_date,
            campground_id,
            user_id
        FROM campground c
        WHERE c.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        campground = Campground(data['id'], data['start_date'], data['end_date'], data['campground_id'], data['user_id'])

    return campground.__dict__
    