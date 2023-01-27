import sqlite3
from models import Campground
from sql_helper import get_all, get_single, create_resource, get_all_by_param

def get_all_campgrounds():
    """Gets all campgrounds
    Returns:
        list: All campground dictionaries"""
    
    sql = """
        SELECT
            c.id,
            c.name,
            c.park_id,
            c.available_sites,
            c.description
        FROM Campgrounds c
        """ 

    campgrounds = []

    dataset = get_all(sql)

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

    sql = """
            SELECT
                c.id,
                c.name,
                c.park_id,
                c.available_sites,
                c.description
            FROM Campgrounds c
            WHERE c.id = ?
            """

    data = get_single(sql, id)

    campground = Campground(data['id'], data['name'], data['park_id'], data['available_sites'], data['description'])

    return campground.__dict__

def create_campground(new_campground):
    """Adds a new campground dictionary

    Args:
        campground (dictionary): Information about the campground

    Returns:
        dictionary: Returns the campground dictionary with a campground id
    """
    sql = """
        INSERT INTO Campgrounds
            ( name, park_id, available_sites, description)
        VALUES
            ( ?, ?, ?, ? );
        """
    
    sql_values = (new_campground['name'], new_campground['park_id'], new_campground['available_sites'], new_campground['description'])

    create_resource(sql, sql_values, new_campground)
    
    return new_campground


def delete_campground(id):
    """Deletes a single campground

    Args:
        id (int): Campground id
    """
    with sqlite3.connect("./national_park.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM campgrounds
        WHERE id = ?
        """, (id, ))

def update_campground(id, new_campground):
    """Updates the campground dictionary with the new values

    Args:
        id (int): Campground id
        new_campground (dict): Campground dictionary with updated values
    """
    with sqlite3.connect("./national_park.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Campgrounds
            SET
                name = ?,
                park_id = ?,
                available_sites = ?,
                description = ?
        WHERE id = ?
        """, (new_campground['name'], new_campground['park_id'], new_campground['available_sites'], new_campground['description'], id, ))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    
    # Forces 204 response by main module
    return True
    
def get_campgrounds_by_park(park_id):
    """Gets all campgrounds by checking for a park_id parameter
    Returns:
        list: All campground dictionaries"""
    
    sql = """
        SELECT
            c.id,
            c.name,
            c.park_id,
            c.available_sites,
            c.description
        FROM Campgrounds c
        WHERE park_id =?
        """ 

    campgrounds = []

    dataset = get_all_by_param(sql, park_id)

    for row in dataset:

        campground = Campground(row['id'], row['name'], row['park_id'], row['available_sites'], row['description'])

        campgrounds.append(campground.__dict__)

    return campgrounds