import sqlite3
from models import Blog

def get_all_blogs():
    """Returns list of all blog dictionaries"""
    with sqlite3.connect("./national_park.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            SELECT
                b.id,
                b.title,
                b.date_created,
                b.user_id,
                b.park_id
            FROM blogs b
            JOIN blog_photos ON
            blogs.id = blog_id
            JOIN photos ON
            photos.id = blog_photos.photo_id
        """)

        blogs = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            blog = Blog(row['id'],row['title'],row['date_created'],row['user_id'],row['park_id'])
            blogs.append(blog.__dict__)
    return blogs


def get_single_blog(id):
    """Returns single blog dictionary by accepting its id as a parameter"""
    with sqlite3.connect("./national_park.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            SELECT
                b.id,
                b.title,
                b.date_created,
                b.user_id,
                b.park_id
            FROM blogs b
            WHERE id = ?
            JOIN blog_photos ON
            blogs.id = blog_id
            JOIN photos ON
            photos.id = blog_photos.photo_id
        """, ( id, ))

        data = db_cursor.fetchone()

        blog = Blog(data['id'], data['title'], data['date_created'],
                    data['user_id'], data['park_id'])

    return blog.__dict__

def get_blog_by_user_id(user_id):
    """Returns a list of all blogs a user has posted by taking the user_id as a parameter"""
    with sqlite3.connect("./national_park.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            SELECT
                b.id,
                b.title,
                b.date_created,
                b.user_id,
                b.park_id
            FROM blogs b
            WHERE user_id = ?
            JOIN blog_photos ON
            blogs.id = blog_id
            JOIN photos ON
            photos.id = blog_photos.photo_id
        """, ( user_id, ))

        data = db_cursor.fetchone()

        blog = Blog(data['id'], data['title'], data['date_created'],
                data['user_id'], data['park_id'])

    return blog.__dict__

def get_blog_by_park_id(park_id):
    """Returns a list of all blogs posted about a park by taking the park_id as a parameter"""
    with sqlite3.connect("./national_park.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            SELECT
                b.id,
                b.title,
                b.date_created,
                b.user_id,
                b.park_id
            FROM blogs b
            WHERE park_id = ?
            JOIN blog_photos ON
            blogs.id = blog_id
            JOIN photos ON
            photos.id = blog_photos.photo_id
        """, ( park_id, ))

        data = db_cursor.fetchone()

        blog = Blog(data['id'], data['title'], data['date_created'],
                    data['user_id'], data['park_id'])

    return blog.__dict__
    
def create_blog(new_blog, new_photo):
    """Creates new blog dictionary"""
    with sqlite3.connect("./national_park.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Blogs
            ( title, post_body, date_created, user_id, park_id )
        VALUES
            ( ?, ?, ?, ?, ?);
        """, (new_blog['title'], new_blog['post_body'],
            new_blog['date_created'], new_blog['user_id'],
            new_blog['park_id'], ))

        new_blog_id = db_cursor.lastrowid
        new_blog['id'] = new_blog_id

        db_cursor.execute("""
        INSERT INTO Photos
            ( url, user_id, park_id )
        VALUES
            ( ?, ?, ? );
        """, (new_photo['url'], new_photo['user_id'],
            new_photo['park_id'] ))

        new_photo_id = db_cursor.lastrowid
        new_photo['id'] = new_photo_id

        new_blog_photo = {}

        db_cursor.execute("""
        INSERT INTO blog_photos
            ( blog_id, photo_id )
        VALUES
            ( ?, ?, ? );
        """, (new_blog_photo['new_blog_id'], new_blog_photo['new_photo_id'] ))

    return new_blog


#not done, good luck figuring out how to also update photos
def update_blog(id, new_blog):
    with sqlite3.connect("./national_park.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Blog
            SET
                title = ?,
                post_body = ?,
                date_created = ?,
                user_id = ?,
                park_id = ?
        WHERE id = ?
        """, (new_blog['title'], new_blog['post_body'],
              new_blog['date_created'], new_blog['user_id'],
              new_blog['park_id'], id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True