import sqlite3
from models import Photos

def get_all_photos():
    "getting all of the photos"
    with sqlite3.connect("./national_park.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            p.id,
            p.url,
            p.user_id,
            p.park_id,
        FROM photos p
        """)

        photos = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            photo = Photos(row['id'], row['url'], row['user_id'], row['park_id'])
            photos.append(photo.__dict__)
        
        return photos

def get_single_photo(id):
    """to get a single photo by id"""
    with sqlite3.connect("./national_park.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            p.id,
            p.url,
            p.user_id,
            p.park_id,
        FROM photos p
        WHERE p.id = ?
        """, ( id, ))

        photos = []

        data = db_cursor.fetchone()

        photo = Photos(data['id'], data['url'], data['user_id'], data['park_id'])

        photos.append(photo.__dict__)

        return photos

