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
        WHERE id = ?
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
