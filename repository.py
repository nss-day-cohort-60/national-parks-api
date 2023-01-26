import sqlite3
from method_mapper import method_mapper
from models import Blog
def all(resource):
    """For GET requests to collection"""
    return method_mapper[resource]["all"]()

def retrieve(resource, id):
    """For GET requests to a single resource"""
    try: #for requests like /something?park_id=3
        parameter = list(id.keys())[0]
        value = list(id.values())[0][0]
    except AttributeError:
        return method_mapper[resource]["single"](id)
    try: # for requests like /something?park_id=3&user_id=1
        second_parameter = list(id.keys())[1]
        second_value = list(id.values())[1][0]
        if resource == "blogs" and parameter == "park_id" and second_parameter == "key_word":
            #needs sql query function in blog_views
            return get_blogs_by_park_id_and_search_term(value, second_value)
        elif resource == "photos" and parameter == "user_id" and second_parameter == "park_id":
            return #a new sql query function from views
    except IndexError:
        return method_mapper[resource][parameter](value)

def create(resource, post_body):
    """For POST requests to a collection"""
    return method_mapper[resource]["post"](post_body)

def update(resource, id, post_body):
    """For PUT requests to a single resource"""
    return method_mapper[resource]["put"](id, post_body)

def delete(resource, id):
    """For DELETE requests to a single resource"""
    return method_mapper[resource]["delete"](id)


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
            WHERE b.park_id = ? AND b.title LIKE ? OR b.post_body LIKE ? 
            """, ( park_id, f"%{search_term}%", f"%{search_term}%"))

        blogs = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            blog = Blog(row['id'],row['title'],row['post_body'],row['date_created'],row['user_id'],row['park_id'], row['photo_url'])
            blogs.append(blog.__dict__)

    return blogs