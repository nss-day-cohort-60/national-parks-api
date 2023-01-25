import sqlite3
from models import Event
from sql_helper import get_all, get_single, create_resource

def get_all_events():
    """Gets all events
    Returns:
        list: All event dictionaries"""
    sql = """
            SELECT
                e.id,
                e.name,
                e.description,
                e.start_date,
                e.park_id
            FROM events e
            """

    events = []

    dataset = get_all(sql)

    for row in dataset:

        event = Event(row['id'], row['name'], row['description'], row['start_date'], row['park_id'])

        events.append(event.__dict__)

    return events

def get_single_event(id):
    """Finds the matching event dictionary for the specified event id

    Args:
        id (int): event id

    Returns:
        dict: event dictionary
    """
    sql = """
            SELECT
            e.id,
                e.name,
                e.description,
                e.start_date,
                e.park_id
            FROM events e
            WHERE e.id = ?
            """

    data = get_single(sql, id)

    event = Event(data['id'], data['name'], data['description'], data['start_date'], data['park_id'])

    return event.__dict__

def create_event(new_event):
    """Adds a new event dictionary

    Args:
        event (dictionary): Information about the event

    Returns:
        dictionary: Returns the event dictionary with an event id
    """
    sql = """
        INSERT INTO events
            (name, description, start_date, park_id)
        VALUES
            ( ?, ?, ?, ?);
        """
    
    sql_values = (new_event['name'], new_event['description'], new_event['start_date'], new_event['park_id'])
    
    create_resource(sql, sql_values, new_event)
    
    return new_event


def delete_event(id):
    """Deletes a single event

    Args:
        id (int): Event id
    """
    with sqlite3.connect("./national_park.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM events
        WHERE id = ?
        """, (id, ))

def update_event(id, new_event):
    """Updates the event dictionary with the new values

    Args:
        id (int): Event id
        new_event (dict): Event dictionary with updated values
    """
    with sqlite3.connect("./national_park.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE events
            SET
                name = ?,
                description = ?,
                start_date = ?,
                park_id = ?
        WHERE id = ?
        """, (new_event['name'], new_event['description'], new_event['start_date'], new_event['park_id'], id, ))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    
    # Forces 204 response by main module
    return True
    