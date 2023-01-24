import sqlite3
from models import Blog
from sql_helper import get_all, get_single

def get_all_blogs():
    """Sends the sql query to get a list of all blog dictionaries to get_all as a parameter

    Returns:
        list: of all blog dictionaries
    """

    sql="""
        SELECT
            b.id,
            b.title,
            b.date_created,
            b.user_id,
            b.park_id,
            b.url
        FROM blogs b
        JOIN blog_photos ON
        blogs.id = blog_id
        JOIN photos ON
        photos.id = blog_photos.photo_id
        """

    blogs = []

    dataset = get_all(sql)

    for row in dataset:
        blog = Blog(row['id'],row['title'],row['date_created'],row['user_id'],row['park_id'])
        blogs.append(blog.__dict__)

    return blogs


def get_single_blog(id):
    """_summary_

    Args:
        id (_type_): _description_

    Returns:
        _type_: _description_
    """    """Returns single blog dictionary by accepting its id as a parameter"""

    sql="""
        SELECT
            b.id,
            b.title,
            b.date_created,
            b.user_id,
            b.park_id,
            b.url
        FROM blogs b
        WHERE blogs.id = ?
        JOIN blog_photos ON
        blogs.id = blog_id
        JOIN photos ON
        photos.id = blog_photos.photo_id
        """

    data = get_single(sql, id)

    blog = Blog(data['id'], data['title'], data['date_created'],
            data['user_id'], data['park_id'])

    return blog.__dict__

def get_blogs_by_user_id(user_id):
    """Accepts user_id as a parameter, then sends it in the sql variable as a parameter to get_all

    Args:
        user_id (int): foreign key for whichever user's blogs you want to look at

    Returns:
        list: of all blogs associated with the user_id foreign key
    """

    sql=("""
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

    blogs = []

    dataset = get_all(sql)

    for row in dataset:
        blog = Blog(row['id'],row['title'],row['date_created'],row['user_id'],row['park_id'])
        blogs.append(blog.__dict__)
    return blogs

def get_blogs_by_park_id(park_id):
    """Accepts park_id as a parameter, then sends it in the sql variable as a parameter to get_all

    Args:
        park_id (int): foreign key for which park the blogs you want to see are associated with

    Returns:
        list: of all blogs associated with the park_id foreign key
    """

    sql=("""
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

    blogs = []

    dataset = get_all(sql)

    for row in dataset:
        blog = Blog(row['id'],row['title'],row['date_created'],row['user_id'],row['park_id'])
        blogs.append(blog.__dict__)
    return blogs

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
