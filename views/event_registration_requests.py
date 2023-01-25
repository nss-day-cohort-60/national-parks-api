import sqlite3 
from models import Registration
from sql_helper import get_all, get_single

def get_all_registration():
    """Gets all event registration
    Returns:
        list: All event registration dictionaries"""
    sql = """
            SELECT
                reg.id,
                reg.event_id,
                reg.user_id
            FROM event_registration reg
            """

    registrations = []

    dataset = get_all(sql)

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
    sql = """
            SELECT
                reg.id,
                reg.event_id,
                reg.user_id
            FROM event_registration reg
            WHERE reg.id = ?
            """

    data = get_single(sql, id)

    registration = Registration(data['id'], data['event_id'], data['user_id'])

    return registration.__dict__

def create_event_registration(new_event_registration):
    """Adds a new event registration dictionary

    Args:
        event_registration (dictionary): Information about the event_registration

    Returns:
        dictionary: Returns the event registration dictionary with an event registration id
    """
    with sqlite3.connect("./national_park.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO event_registration
            (event_id, user_id)
        VALUES
            ( ?, ?);
        """, (new_event_registration['event_id'], new_event_registration['user_id'], ))
        
        id = db_cursor.lastrowid

        new_event_registration['id'] = id
    
    return new_event_registration


def delete_event_registration(id):
    """Deletes a single event_registration

    Args:
        id (int): Event_registration id
    """
    with sqlite3.connect("./national_park.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM event_registration
        WHERE id = ?
        """, (id, ))

def update_event_registration(id, new_event_registration):
    """Updates the event_registration dictionary with the new values

    Args:
        id (int): Event_registration id
        new_event_registration (dict): Event_registration dictionary with updated values
    """
    with sqlite3.connect("./national_park.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE event_registration
            SET
                event_id = ?,
                user_id = ?,
        WHERE id = ?
        """, (new_event_registration['event_id'], new_event_registration['user_id'], id, ))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    
    # Forces 204 response by main module
    return True
    