from models import Photos, User
from sql_helper import get_all, get_single, get_all_by_param

def get_all_photos():
    """Gets all photos
    Returns:
        list: All photo dictionaries"""

    sql = """
        SELECT
            p.id,
            p.url,
            p.user_id,
            p.park_id
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
            p.park_id
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

    sql="""
        SELECT
            p.id,
            p.url,
            p.user_id,
            p.park_id
        FROM photos p
        WHERE user_id = ?
        """

    photos = []

    dataset = get_all_by_param(sql, user_id)

    for row in dataset:
        photo = Photos(row['id'], row['url'], row['user_id'], row['park_id'])
        photos.append(photo.__dict__)

    return photos

def create_photos(photo):
    with sqlite3.connect("./national_park.sqlite3") as conn:
        db_cursor = conn.cursor()
        # set: returns the unique values of list of values, wrapped in curly braces
        # often convert to list: list(set(value_list))
        if all(val for val in photo.values()) and set(photo.keys()) == {'url', 'user_id', 'park_id'}:
            db_cursor.execute("""
            INSERT INTO Photos
                ( url, user_id, park_id )
            VALUES
                ( ?, ?, ?, ?, ?);
            """, (photo['url'], photo['user_id'], photo['park_id'] ))

            id = db_cursor.lastrowid

            photo['id'] = id

            return photo
        else:
            return "missing information"

def get_photos_by_park_id(park_id):
    """Accepts park_id as a parameter, then sends it in the sql variable as a parameter to get_all

    Args:
        park_id (int): foreign key for which park the photos you want to see are associated with

    Returns:
        list: of all photos associated with the park_id foreign key
    """

    sql="""
        SELECT
            p.id,
            p.url,
            p.user_id,
            p.park_id
        FROM photos p
        WHERE park_id = ?
        """

    photos = []

    dataset = get_all_by_param(sql, park_id)

    for row in dataset:
        photo = Photos(row['id'], row['url'], row['user_id'], row['park_id'])
        photos.append(photo.__dict__)

    return photos

