import sqlite3
from models import Amenity, ParkAmenity
from sql_helper import get_all, get_single

def get_all_amenity_types():
    """fetches list of amenity types from amenities table"""
    sql = (
        """
        SELECT
            a.id,
            a.type
        FROM Amenities a
        """
    )

    amenity_types = []
    dataset = get_all(sql)

    for row in dataset:
        amenity = Amenity(row["id"], row["type"])

        amenity_types.append(amenity.__dict__)

    return amenity_types

def get_amenity_type_by_id(id):
    """fetches list of amenity types from amenities table"""
    sql = (
        """
        SELECT
            a.id,
            a.type
        FROM Amenities a
        WHERE id = ?
        """
    )

    amenity = {}
    data = get_single(sql, id)
    amenity = Amenity(data["id"], data["type"])

    return amenity.__dict__

def get_all_amenities():
    """fetches list of amenity types from amenities table"""
    sql = (
        """
        SELECT
            pa.id,
            pa.name,
            pa.amenity_id,
            pa.park_id
        FROM Park_Amenities pa
        """
    )

    amenities = []
    dataset = get_all(sql)

    for row in dataset:
        park_amenity = ParkAmenity(row["id"], row["name"], row["amenity_id"], row["park_id"])

        amenities.append(park_amenity.__dict__)

    return amenities

def get_amenity_by_id(id):
    """fetches list of amenity types from amenities table"""
    sql = (
        """
        SELECT
            pa.id,
            pa.name,
            pa.amenity_id,
            pa.park_id
        FROM Park_Amenities pa
        WHERE id = ?
        """
    )

    park_amenity = {}
    data = get_single(sql, id)
    park_amenity = ParkAmenity(data["id"], data["name"], data["amenity_id"], data["park_id"])

    return park_amenity.__dict__

def create_amenity_type(new_amenity_type):
    """Posts a new dictionary of class Amenity to the database, given type property

    new_amenity_type: type: ""
    """
    with sqlite3.connect("./national_park.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Amenities
            ( type )
        VALUES
            ( ? );
        """, ( new_amenity_type['type'], ))

        new_amenity_type['id'] = db_cursor.lastrowid

    return new_amenity_type

def create_park_amenity(new_park_amenity):
    """Posts a new dictionary of class ParkAmenity to the database, given all properties

    new_park_amenity: name: "" (nullable), amenity_id: (int), park_id: (int)
    """
    with sqlite3.connect("./national_park.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Park_Amenities
            ( name, amenity_id, park_id )
        VALUES
            ( ?, ?, ?);
        """, ( new_park_amenity['name'], new_park_amenity['amenity_id'], new_park_amenity['park_id'] ))

        new_park_amenity['id'] = db_cursor.lastrowid

    return new_park_amenity

def update_amenity_type(id, new_amenity_type):
    """Updates dictionary of class Amenity in the database, given type property

    new_amenity_type: type: ""
    """

    with sqlite3.connect("./national_park.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Amenities
            SET
            type = ?
        WHERE id = ?;
        """, ( new_amenity_type['type'], id ))

    return new_amenity_type

def update_park_amenity(id, new_park_amenity):
    """Posts a new dictionary of class ParkAmenity to the database, given all properties

    new_park_amenity: name: "" (nullable), amenity_id: (int), park_id: (int)
    """
    with sqlite3.connect("./national_park.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Park_Amenities
            SET
            name = ?,
            amenity_id = ?,
            park_id =?
        WHERE id = ?
        """, ( new_park_amenity['name'], new_park_amenity['amenity_id'], new_park_amenity['park_id'], id ))

    return new_park_amenity

def delete_park_amenity(id):
    """Deletes a park amenity from Park_Amenities database table, given an id

    Args: id (int)
    """
    with sqlite3.connect("./national_park.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Park_Amenities
        WHERE id = ?
        """, ( id, ))

def delete_amenity_type(id):
    """Deletes an amenity type from Amenities database table, given an id

    Args: id (int)
    """
    with sqlite3.connect("./national_park.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Amenities
        WHERE id = ?
        """, ( id, ))
