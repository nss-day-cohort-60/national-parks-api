from models import Parks
from sql_helper import get_all, get_single

def get_all_parks():
    """Gets all parks
        Returns: a list of all park dictionaries"""

    sql= """
        SELECT
            p.id,
            p.name,
            p.history,
            p.city,
            p.state,
            p.latitude,
            p.longitude,
        FROM parks p
        """

    parks = []

    dataset = get_all(sql)

    for row in dataset:
        park = Parks(row['id'], row['name'], row['history'], row['city'], row['state'], row['latitude'], row['longitude'])
        parks.append(park.__dict__)
        
    return parks

def get_single_park(id):
    """finds the matching park dictionary for the specified park id"""
    sql = """
        SELECT
            p.id,
            p.name,
            p.history,
            p.city,
            p.state,
            p.latitude,
            p.longitude,
        FROM parks p
        WHERE p.id = ?
        """

    data = get_single(sql, id)

    park = Parks(data['id'], data['name'], data['history'], data['city'], data['state'], data['latitude'], data['longitude'])

    return park.__dict__
