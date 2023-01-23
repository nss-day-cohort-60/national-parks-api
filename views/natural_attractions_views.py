import sqlite3
from models import Natural_Attraction


def get_all_natural_attractions():
    """Function to retrieve all natural_attractions from a database and return the data as a list of dictionaries"""
    with sqlite3.connect("./national_park.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT 
        n.id,
        n.name
        FROM Natural_Attractions n
        """)

        natural_attractions = []

        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:
            natural_attraction = Natural_Attraction(row['id'], row['name'])

            natural_attractions.append(natural_attraction.__dict__)

    return natural_attractions


def get_single_natural_attraction(id):
    with sqlite3.connect("./national_park.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT 
        n.id,
        n.name
        FROM Natural_Attractions n
        WHERE n.id = ?
        """, (id, ))

        data = db_cursor.fetchone()
        if not data:
            return {}
        natural_attraction = Natural_Attraction(data['id'], data['name'])

        return natural_attraction.__dict__
