from models import Parks
from sql_helper import get_all, get_single
import sqlite3

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
            p.longitude
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
            p.longitude
        FROM parks p
        WHERE p.id = ?
        """

    data = get_single(sql, id)

    park = Parks(data['id'], data['name'], data['history'], data['city'], data['state'], data['latitude'], data['longitude'])

    return park.__dict__

def create_park(park):
    """creating a post request to create a park. Checks if all values are included in post, returns error"""
    with sqlite3.connect("./national_park.sqlite3") as conn:
        db_cursor = conn.cursor()
        # set: returns the unique values of list of values, wrapped in curly braces
        # often convert to list: list(set(value_list))
        if all(val for val in park.values()) and set(park.keys()) == {'url', 'user_id', 'park_id'}:
            db_cursor.execute("""
            INSERT INTO Parks
                ( url, user_id, park_id )
            VALUES
                ( ?, ?, ?, ?, ?, ?);
            """, (park['name'], park['history'], park['city'], park['state'], park['longitude'], park['latitude'] ))

            id = db_cursor.lastrowid

            park['id'] = id

            return park
        else:
            return "missing information"

