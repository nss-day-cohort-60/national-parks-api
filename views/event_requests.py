import sqlite3
from models import Event

def get_all_events():
    """Gets all events
    Returns:
        dict: All event dictionaries"""
    with sqlite3.connect("./national_park.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.description,
            e.start_date,
            e.park_id
        FROM event e
        """)

        events = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            event = Event(row['id'], row['name'], row['description'], row['start_date'], row['park_id'])

            events.append(event.__dict__)

    return events

def get_single_event():
    """Finds the matching event dictionary for the specified event id

    Args:
        id (int): event id

    Returns:
        object: event dictionary
    """
    with sqlite3.connect("./national_park.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
           e.id,
            e.name,
            e.description,
            e.start_date,
            e.park_id
        FROM event e
        WHERE e.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        event = Event(data['id'], data['name'], data['description'], data['start_date'], data['park_id'])

    return event.__dict__
    
    