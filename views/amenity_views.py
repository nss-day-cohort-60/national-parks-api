import sqlite3
from models import Amenity, Park_Amenity
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
        park_amenity = Park_Amenity(row["id"], row["name"], row["amenity_id"], row["park_id"])

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
    park_amenity = Park_Amenity(data["id"], data["name"], data["amenity_id"], data["park_id"])

    return park_amenity.__dict__
