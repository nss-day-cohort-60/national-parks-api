import sqlite3
from models import Reservation

def get_all_reservations():
    """Gets all campground reservations
    Returns:
        dict: All campground reservation dictionaries"""
    with sqlite3.connect("./national_park.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            res.id,
            res.start_date,
            res.end_date,
            res.campground_id,
            res.user_id
        FROM camping_reservations res
        """)

        reservations = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            reservation = Reservation(row['id'], row['start_date'], row['end_date'], row['campground_id'], row['user_id'])

            reservations.append(reservation.__dict__)

    return reservations

def get_single_reservation():
    """Finds the matching reservation dictionary for the specified reservation id

    Args:
        id (int): reservation id

    Returns:
        object: reservation dictionary
    """
    with sqlite3.connect("./national_park.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            res.id,
            res.start_date,
            res.end_date,
            res.campground_id,
            res.user_id
        FROM camping_reservations res
        WHERE res.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        reservation = Reservation(data['id'], data['start_date'], data['end_date'], data['campground_id'], data['user_id'])

    return reservation.__dict__
    