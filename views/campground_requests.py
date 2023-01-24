from models import Campground
from sql_helper import get_all, get_single

def get_all_campgrounds(sql):
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
        FROM Campground c
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
            c.start_date,
            c.end_date,
            campground_id,
            user_id
            FROM campground c
            WHERE c.id = ?
            """

    data = get_single(sql, id)

    campground = Campground(data['id'], data['start_date'], data['end_date'], data['campground_id'], data['user_id'])

    return campground.__dict__
    