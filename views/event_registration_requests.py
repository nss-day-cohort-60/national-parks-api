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

    