import sqlite3
from models import Natural_Attraction
from sql_helper import get_all, get_single

def get_all_natural_attractions():
    """Function to retrieve all natural_attractions from a database and return the data as a list of dictionaries"""
    sql = (
    """
        SELECT
            n.id,
            n.name
        FROM Natural_Attractions n
    """)

    natural_attractions = []

    dataset = get_all(sql)

    # Iterate list of data returned from database
    for row in dataset:
        natural_attraction = Natural_Attraction(row['id'], row['name'])

        natural_attractions.append(natural_attraction.__dict__)

    return natural_attractions

def get_single_natural_attraction(id):
    """A function that retrieves a single natural_attraction based on the given id"""
    sql = (
    """
        SELECT
            n.id,
            n.name
        FROM Natural_Attractions n
        WHERE n.id = ?
    """)

    data = get_single(sql, id)
    if not data:
        return {}
    natural_attraction = Natural_Attraction(data['id'], data['name'])

    return natural_attraction.__dict__
