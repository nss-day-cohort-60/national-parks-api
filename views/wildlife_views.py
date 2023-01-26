import sqlite3
from models import Wildlife
from sql_helper import get_all, get_single, get_all_by_param, create_resource, update_resource, delete_resource


def get_all_wildlife():
    """Function to retrieve all wildlife from a database and return the data as a list of dictionaries"""
    sql = """
            SELECT 
            w.id,
            w.name,
            w.information,
            w.wildlife_group_id,
            w.image
            FROM wildlife w
            """

    all_wildlife = []
    
    dataset = get_all(sql)

    for row in dataset:
        wildlife = Wildlife(row['id'], row['name'], row['information'],
                            row['wildlife_group_id'], row['image'])

        all_wildlife.append(wildlife.__dict__)

    return all_wildlife


def get_single_wildlife_type(id):
    """A function that retrieves a single wildlife type based on the given id"""
    sql = """
            SELECT 
            w.id,
            w.name,
            w.information,
            w.wildlife_group_id,
            w.image
            FROM wildlife w
            WHERE w.id = ?
            """

    data = get_single(sql, id)
    
    if not data:
        return {}

    wildlife = Wildlife(data['id'], data['name'], data['information'],
                        data['wildlife_group_id'], data['image'])

    return wildlife.__dict__


def get_wildlife_by_park_id(park_id):
    """getting all wildlife in a specific park"""

    sql = """
        SELECT
            w.id,
            w.name,
            w.information,
            w.wildlife_group_id,
            w.image
        FROM Park_Wildlife pw
        JOIN Wildlife w
            ON pw.wildlife_id = w.id
        WHERE pw.park_id = ?
		ORDER BY w.name ASC;
    """

    all_wildlife = []

    dataset = get_all_by_param(sql, park_id)
    if dataset is None:
        return []
    for row in dataset:
        wildlife = Wildlife(row['id'], row['name'], row['information'],
                            row['wildlife_group_id'], row['image'])

        result = wildlife.__dict__
        all_wildlife.append(result)
    return all_wildlife

def create_wildlife(new_wildlife):
    """Function to create a new resource in the database"""
    sql = """   
        INSERT INTO Wildlife
            ( name, information, wildlife_group_id, image)
        VALUES
            ( ?, ?, ?, ?);
        """     
    sql_values = (new_wildlife['name'], new_wildlife['information'],
              new_wildlife['wildlife_group_id'], new_wildlife['image'])

    new_resource = create_resource(sql, sql_values, new_wildlife)

    return new_resource

def update_wildlife(id, new_wildlife):
    """Function to update the Wildlife table in a database"""
    sql = """
        UPDATE Wildlife
            SET
                name = ?,
                information = ?,
                wildlife_group_id = ?,
                image = ?
        WHERE id = ?
        """
    sql_values = (new_wildlife['name'], new_wildlife['information'],new_wildlife['wildlife_group_id'], new_wildlife['image'], id,) 

    rows_affected = update_resource(sql, sql_values)

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
        # Forces 204 response by main module
    return True

def delete_wildlife(id):
    """remove wildlife dictionary from the list"""
    sql = """
        DELETE FROM Wildlife
        WHERE id = ?
        """
    delete_resource(sql, id)
