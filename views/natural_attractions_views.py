import sqlite3
from models import NaturalAttraction, ParkNaturalAttraction
from sql_helper import get_all, get_single, get_all_by_param, create_resource, update_resource, delete_resource

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
        natural_attraction = NaturalAttraction(row['id'], row['name'])

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
    natural_attraction = NaturalAttraction(data['id'], data['name'])

    return natural_attraction.__dict__

def get_natural_attraction_by_park_id(park_id):
    """getting all natural attractions in a specific park"""

    sql = """
    SELECT
        pna.id,
        pna.name as natural_attraction_name,
        pna.description,
        pna.park_id,
        pna.attraction_id,
        p.name as park_name
    FROM Park_Natural_Attractions pna
    JOIN Parks p
        ON pna.park_id = p.id
    WHERE pna.park_id = ?
    """

    park_natural_attractions = []

    dataset = get_all_by_param(sql, park_id)
    if dataset is None:
        return []
    for row in dataset:
        park_natural_attraction = ParkNaturalAttraction(
            row['id'], row['natural_attraction_name'], row['description'], row['park_id'], row['attraction_id'])
        result = park_natural_attraction.__dict__
        # add park_name key to the dictionary:
        result['park_name'] = row['park_name']
        park_natural_attractions.append(result)
        
    return park_natural_attractions

def create_natural_attraction(new_attraction):
    """Function to create a new resource in the database"""

    sql = """
        INSERT INTO Natural_Attractions
            ( name)
        VALUES
            ( ?);
        """
    sql_values =(new_attraction['name'],)

    new_resource = create_resource(sql, sql_values, new_attraction)

    return new_resource


def update_natural_attraction(id, new_attraction):
    """Function to update the Natural_Attractions table in a database"""

    sql = """
        UPDATE Natural_Attractions
            SET
                name = ?
        WHERE id = ?
        """ 
    sql_values = (new_attraction['name'], id, )

        # Were any rows affected?
        # Did the client send an `id` that exists?
        
    return update_resource(sql, sql_values)


   

def delete_natural_attraction(id):
    """remove natural_attraction dictionary from the list"""
  
    sql = """
        DELETE FROM Natural_Attractions
        WHERE id = ?
        """
    delete_resource(sql, id)
