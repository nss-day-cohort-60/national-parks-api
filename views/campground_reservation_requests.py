from models import Reservation
from sql_helper import get_all, get_single

def get_all_reservations():
    """Gets all campground reservations
    Returns:
        list: All campground reservation dictionaries"""
    sql = """
            SELECT
                res.id,
                res.start_date,
                res.end_date,
                res.campground_id,
                res.user_id
            FROM camping_reservations res
            """

    reservations = []

    dataset = get_all(sql)

    for row in dataset:

        reservation = Reservation(row['id'], row['start_date'], row['end_date'], row['campground_id'], row['user_id'])

        reservations.append(reservation.__dict__)

    return reservations
    
def get_single_reservation(id):
    """Finds the matching reservation dictionary for the specified reservation id

    Args:
        id (int): reservation id

    Returns:
        dict: reservation dictionary
    """
    sql = """
            SELECT
                res.id,
                res.start_date,
                res.end_date,
                res.campground_id,
                res.user_id
            FROM camping_reservations res
            WHERE res.id = ?
            """, ( id, )

    data = get_single(sql, id)

    reservation = Reservation(data['id'], data['start_date'], data['end_date'], data['campground_id'], data['user_id'])

    return reservation.__dict__
    