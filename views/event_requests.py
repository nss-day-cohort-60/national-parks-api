from models import Event
from sql_helper import get_all, get_single

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
            FROM event e
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
            FROM event e
            WHERE e.id = ?
            """

    data = get_single(sql, id)

    event = Event(data['id'], data['name'], data['description'], data['start_date'], data['park_id'])

    return event.__dict__
    
    