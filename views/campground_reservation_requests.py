import sqlite3
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
                res.campround_id,
                res.user_id
            FROM camping_reservations res
            """

    reservations = []

    dataset = get_all(sql)

    for row in dataset:

        reservation = Reservation(row['id'], row['start_date'], row['end_date'], row['campround_id'], row['user_id'])

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
                res.campround_id,
                res.user_id
            FROM camping_reservations res
            WHERE res.id = ?
            """

    data = get_single(sql, id)

    reservation = Reservation(data['id'], data['start_date'], data['end_date'], data['campround_id'], data['user_id'])

    return reservation.__dict__

def create_reservation(new_reservation):
    """Adds a new reservation dictionary

    Args:
        reservation (dictionary): Information about the reservation

    Returns:
        dictionary: Returns the reservation dictionary with a reservation id
    """
    with sqlite3.connect("./national_park.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO camping_reservations
            ( start_date, end_date, campround_id, user_id)
        VALUES
            ( ?, ?, ?, ? );
        """, (new_reservation['start_date'], new_reservation['end_date'], new_reservation['campground_id'], new_reservation['user_id'], ))
        
        id = db_cursor.lastrowid

        new_reservation['id'] = id
    
    return new_reservation


def delete_reservation(id):
    """Deletes a single reservation

    Args:
        id (int): Reservation id
    """
    with sqlite3.connect("./national_park.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM camping_reservations
        WHERE id = ?
        """, (id, ))

def update_reservation(id, new_reservation):
    """Updates the reservation dictionary with the new values

    Args:
        id (int): Reservation id
        new_reservation (dict): Reservation dictionary with updated values
    """
    with sqlite3.connect("./national_park.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE camping_reservations
            SET
                start_date = ?,
                end_date = ?,
                campround_id = ?,
                user_id = ?
        WHERE id = ?
        """, (new_reservation['start_date'], new_reservation['end_date'], new_reservation['campground_id'], new_reservation['user_id'], id, ))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    
    # Forces 204 response by main module
    return True
    
    