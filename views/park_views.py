from models import Parks
import sqlite3

def get_all_parks():
    """getting all of the parks and their data"""
    with sqlite3.connect("./national_park.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            p.id,
            p.name,
            p.history,
            p.city,
            p.state,
            p.latitude,
            p.longitude,
        FROM parks p
        """)

        parks = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            park = Parks(row['id'], row['name'], row['history'], row['city'], row['state'], row['latitude'], row['longitude'])
            parks.append(park.__dict__)
        
        return parks

def get_single_park(id):
    """getting one park by id"""
    with sqlite3.connect("./national_park.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
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
        """, ( id, ))

        parks = []

        data = db_cursor.fetchone()

        park = Parks(data['id'], data['name'], data['history'], data['city'], data['state'], data['latitude'], data['longitude'])

        parks.append(park.__dict__)

        return parks
