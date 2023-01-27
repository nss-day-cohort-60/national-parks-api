import sqlite3
from models import Blog
import datetime
from sql_helper import get_all, get_single, create_resource, get_all_by_param

def get_all_blogs():
    """Sends the sql query to get a list of all blog dictionaries to get_all as a parameter

    Returns:
        list: of all blog dictionaries
    """

    sql="""
        SELECT
            b.id,
            b.title,
            b.post_body,
            b.date_created,
            b.user_id,
            b.park_id,
            p.url as photo_url
        FROM Blogs b
        LEFT JOIN Blog_Photos bp ON
        b.id = bp.blog_id
        LEFT JOIN Photos p ON
        p.id = bp.photo_id
        ORDER BY b.date_created DESC
        """

    blogs = []

    dataset = get_all(sql)

    for row in dataset:
        blog = Blog(row['id'],row['title'],row['post_body'],row['date_created'],row['user_id'],row['park_id'], row['photo_url'])
        blogs.append(blog.__dict__)

    return blogs


def get_single_blog(id):
    """Returns a single blog dictionary

    Args:
        id (int): primary key for the blog being requested

    Returns:
        dict: the blog dictionary in question
    """

    sql="""
        SELECT
            b.id,
            b.title,
            b.post_body,
            b.date_created,
            b.user_id,
            b.park_id,
            p.url as photo_url
        FROM Blogs b
        LEFT JOIN Blog_Photos bp ON
        b.id = bp.blog_id
        LEFT JOIN photos p ON
        p.id = bp.photo_id
        WHERE b.id = ?
        """

    data = get_single(sql, id)

    blog = Blog(data['id'], data['title'], data['post_body'], data['date_created'],
            data['user_id'], data['park_id'], data['photo_url'])

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
            b.post_body,
            b.date_created,
            b.user_id,
            b.park_id,
            p.url as photo_url
        FROM blogs b
        LEFT JOIN blog_photos ON
        b.id = blog_id
        LEFT JOIN photos p ON
        p.id = blog_photos.photo_id
        WHERE b.user_id = ?
        """)

    blogs = []

    dataset = get_all_by_param(sql, user_id)

    for row in dataset:
        blog = Blog(row['id'],row['title'],row['post_body'],row['date_created'],row['user_id'],row['park_id'],row['photo_url'])
        
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
            b.post_body,
            b.date_created,
            b.user_id,
            b.park_id,
            p.url as photo_url
        FROM blogs b
        LEFT JOIN blog_photos ON
        b.id = blog_id
        LEFT JOIN photos p ON
        p.id = blog_photos.photo_id
        WHERE b.park_id = ?
        """)

    blogs = []

    dataset = get_all_by_param(sql, park_id)

    for row in dataset:
        blog = Blog(row['id'],row['title'],row['post_body'],row['date_created'],row['user_id'],row['park_id'],row['photo_url'])
        
        blogs.append(blog.__dict__)

    return blogs

def create_blog(new_blog):
    """Creates new blog dictionary"""

    date_created = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    sql="""
        INSERT INTO Blogs
            ( title, post_body, date_created, user_id, park_id, photo_id )
        VALUES
            ( ?, ?, ?, ?, ?, ?);
        """
    sql_values=(new_blog['title'], new_blog['post_body'], date_created, new_blog['user_id'], new_blog['park_id'], new_blog['photo_id'])

    new_resource = create_resource(sql, sql_values, new_blog)

    return new_resource


#not done, good luck figuring out how to also update photos
def update_blog(id, new_blog):
    with sqlite3.connect("./national_park.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Blogs
            SET
                title = ?,
                post_body = ?,
                date_created = ?,
                user_id = ?,
                park_id = ?
        WHERE id = ?
        """, (new_blog['title'], new_blog['post_body'], new_blog['date_created'], new_blog['user_id'], new_blog['park_id'], id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True

def delete_blog(id):

    sql = """
    DELETE FROM Blogs
    WHERE id = ?
    """

    get_single(sql, id)

def get_blogs_by_park_id_and_search_term(park_id, search_term):
    """Sends the sql query to get a list of all blog dictionaries to get_all as a parameter

    Returns:
        list: of all blog dictionaries
    """

    with sqlite3.connect("./national_park.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
            SELECT
                b.id,
                b.title,
                b.post_body,
                b.date_created,
                b.user_id,
                b.park_id,
                p.url as photo_url
            FROM Blogs b
            LEFT JOIN Blog_Photos bp ON
            b.id = bp.blog_id
            LEFT JOIN Photos p ON
            p.id = bp.photo_id
            WHERE b.park_id = ? AND (b.title LIKE ? OR b.post_body LIKE ?)
            """, ( park_id, f"%{search_term}%", f"%{search_term}%"))

        blogs = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            blog = Blog(row['id'],row['title'],row['post_body'],row['date_created'],row['user_id'],row['park_id'], row['photo_url'])
            blogs.append(blog.__dict__)

    return blogs

def get_blogs_by_search_term(search_term):
    """Sends the sql query to get a list of all blog dictionaries to get_all as a parameter

    Returns:
        list: of all blog dictionaries
    """

    with sqlite3.connect("./national_park.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
            SELECT
                b.id,
                b.title,
                b.post_body,
                b.date_created,
                b.user_id,
                b.park_id,
                p.url as photo_url
            FROM Blogs b
            LEFT JOIN Blog_Photos bp ON
            b.id = bp.blog_id
            LEFT JOIN Photos p ON
            p.id = bp.photo_id
            WHERE b.title LIKE ? OR b.post_body LIKE ?
            """, ( f"%{search_term}%", f"%{search_term}%"))

        blogs = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            blog = Blog(row['id'],row['title'],row['post_body'],row['date_created'],row['user_id'],row['park_id'], row['photo_url'])
            blogs.append(blog.__dict__)

    return blogs