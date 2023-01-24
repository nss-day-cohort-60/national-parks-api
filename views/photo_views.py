from models import Photos
from sql_helper import get_all, get_single

def get_all_photos():
    """Gets all photos
    Returns:
        list: All photo dictionaries"""

    sql = """
        SELECT
            p.id,
            p.url,
            p.user_id,
            p.park_id,
        FROM photos p
        """

    photos = []

    dataset = get_all(sql)

    for row in dataset:
        photo = Photos(row['id'], row['url'], row['user_id'], row['park_id'])
        photos.append(photo.__dict__)

    return photos

def get_single_photo(id):
    """Finds the matching photo dictionary for the specified photo id

    Args:
        id (int): photo id

    Returns:
        dict: photo dictionary
    """

    sql = """
        SELECT
            p.id,
            p.url,
            p.user_id,
            p.park_id,
        FROM photos p
        WHERE p.id = ?
        """

    data = get_single(sql, id)

    photo = Photos(data['id'], data['url'], data['user_id'], data['park_id'])

    return photo.__dict__

def get_photos_by_user_id(user_id):
    """Accepts user_id as a parameter, then sends it in the sql variable as a parameter to get_all

    Args:
        user_id (int): foreign key to show each user their own uploaded images

    Returns:
        list: of all photos associated with the user_id foreign key
    """

    sql=("""
       SELECT
            p.id,
            p.url,
            p.user_id,
            p.park_id,
        FROM photos p
        WHERE user_id = ?
        """, ( user_id, ))

    photos = []

    dataset = get_all(sql)

    for row in dataset:
        photo = Photos(row['id'], row['url'], row['user_id'], row['park_id'])
        photos.append(photo.__dict__)       
    return photos
