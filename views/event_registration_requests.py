import sqlite3
from models import Registration

def get_all_registration():
    """Gets all event registration
    Returns:
        list: All event registration dictionaries"""
    with sqlite3.connect("./national_park.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            reg.id,
            reg.event_id,
            reg.user_id
        FROM event_registration reg
        """)

        registrations = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            registration = Registration(row['id'], row['event_id'], row['user_id'])

            registrations.append(registration.__dict__)

    return registrations

def get_single_registration(id):
    """Finds the matching event registration dictionary for the specified event registration id

    Args:
        id (int): event registration id

    Returns:
        dict: event registration dictionary
    """
    with sqlite3.connect("./national_park.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            reg.id,
            reg.event_id,
            reg.user_id
        FROM event_registration reg
        WHERE reg.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        registration = Registration(data['id'], data['event_id'], data['user_id'])

    return registration.__dict__

    