import sqlite3
from models import Amenity, Park_Amenity

def get_all_amenity_types():
    """fetches list of amenity types from amenities table"""
    with sqlite3.connect("./national_park.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute(
            """
        SELECT
            *
        FROM Amenities
        """
        )

        amenity_types = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            amenity = Amenity(row["id"], row["type"])

            amenity_types.append(amenity.__dict__)

    return amenity_types

def get_amenity_type_by_id(id):
    """fetches list of amenity types from amenities table"""
    with sqlite3.connect("./national_park.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute(
            """
        SELECT
            *
        FROM Amenities
        WHERE id = ?
        """, (id, )
        )

        amenity = {}
        data = db_cursor.fetchone()
        amenity = Amenity(data["id"], data["type"])

    return amenity.__dict__

def get_all_amenities():
    """fetches list of amenity types from amenities table"""
    with sqlite3.connect("./national_park.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute(
            """
        SELECT
            *
        FROM Park_Amenities
        """
        )

        amenities = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            park_amenity = Park_Amenity(row["id"], row["name"], row["amenity_id"], row["park_id"])

            amenities.append(park_amenity.__dict__)

    return amenities

def get_amenity_by_id(id):
    """fetches list of amenity types from amenities table"""
    with sqlite3.connect("./national_park.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute(
            """
        SELECT
            *
        FROM Park_Amenities
        WHERE id = ?
        """, (id, )
        )

        park_amenity = {}
        data = db_cursor.fetchone()
        park_amenity = Park_Amenity(data["id"], data["name"], data["amenity_id"], data["park_id"])

    return park_amenity.__dict__
