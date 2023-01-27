import sqlite3
from models import User, UserFavorite
from sql_helper import get_all, get_single, get_all_by_param

def get_all_users():
    """fetches list of amenity types from amenities table"""
    sql =(
        """
        SELECT
            u.id,
            u.first_name,
            u.last_name,
            u.email,
            u.password,
            u.isRanger
        FROM Users u
        """
    )

    users = []
    dataset = get_all(sql)

    for row in dataset:
        user = User(row["id"], row["first_name"], row["last_name"], row["email"], row["password"], row["isRanger"])

        users.append(user.__dict__)

    return users

def get_user_by_id(id):
    """fetches list of amenity types from amenities table"""
    sql = (
        """
        SELECT
            u.id,
            u.first_name,
            u.last_name,
            u.email,
            u.password,
            u.isRanger
        FROM Users u
        WHERE id = ?
        """
    )

    user = {}
    row = get_single(sql, id)
    user = User(row["id"], row["first_name"], row["last_name"], row["email"], row["password"], row["isRanger"])

    return user.__dict__

def get_user_by_email(email):
    """fetches list of amenity types from amenities table"""
    sql = (
        """
        SELECT
            u.id,
            u.first_name,
            u.last_name,
            u.email,
            u.password,
            u.isRanger
        FROM Users u
        WHERE email = ?
        """
    )

    user = {}
    try:
        row = get_all_by_param(sql, email)[0]
        user = User(row["id"], row["first_name"], row["last_name"], row["email"], row["password"], row["isRanger"])
        return user.__dict__
    except IndexError:
        return None

def update_user(id, new_user):
    """Posts a new dictionary of class User to the database, given all User properties

    new_user: first_name: "", last_name: "", email: "", password: "", isRanger: bool
    """

    with sqlite3.connect("./national_park.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Users
            SET
            first_name = ?,
            last_name = ?,
            email = ?,
            password = ?,
            isRanger = ?
        WHERE id = ?;
        """, ( new_user['first_name'], new_user['last_name'], new_user['email'], new_user['password'], new_user['isRanger'], id ))

    new_user['id'] = id

    return new_user

def create_user(new_user):
    """Posts a new dictionary of class User to the database, given all User properties

    new_user: first_name: "", last_name: "", email: "", password: "", isRanger: bool
    """

    with sqlite3.connect("./national_park.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Users
            ( first_name, last_name, email, password, isRanger )
        VALUES
            ( ?, ?, ?, ?, ?);
        """, ( new_user['first_name'], new_user['last_name'], new_user['email'], new_user['password'], new_user['isRanger'] ))

        new_user['id'] = db_cursor.lastrowid

    return new_user

def get_all_user_favorites():
    """fetches list of amenity types from amenities table"""
    sql = (
        """
        SELECT
            uf.id,
            uf.type_id,
            uf.post_id,
            uf.user_id
        FROM User_Favorites uf
        """
    )

    favorites = []
    dataset = get_all(sql)

    for row in dataset:
        favorite = UserFavorite(row["id"], row["type_id"], row["post_id"], row["user_id"])

        favorites.append(favorite.__dict__)

    return favorites

def get_user_favorite_by_id(id):
    """fetches list of amenity types from amenities table"""
    sql = (
        """
        SELECT
            uf.id,
            uf.type_id,
            uf.post_id,
            uf.user_id
        FROM User_Favorites uf
        WHERE id = ?
        """
    )

    favorite = {}
    row = get_single(sql, id)
    favorite = UserFavorite(row["id"], row["type_id"], row["post_id"], row["user_id"])

    return favorite.__dict__

def create_user_favorite(new_favorite):
    """Posts a new dictionary of class UserFavorite to the database, given all properties

    new_favorite: type_id: "", post_id: "", user_id: "", password: "", isRanger: bool
    """

    with sqlite3.connect("./national_park.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO User_Favorites
            ( type_id, post_id, user_id )
        VALUES
            ( ?, ?, ? );
        """, ( new_favorite['type_id'], new_favorite['post_id'], new_favorite['user_id'] ))

        new_favorite['id'] = db_cursor.lastrowid

    return new_favorite

def delete_user(id):
    """Deletes a dictionary of class User from the database, given an id

    Args: id (int)
    """

    with sqlite3.connect("./national_park.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Users
        WHERE id = ?
        """, ( id, ))

def delete_user_favorite(id):
    """Deletes a dictionary of class UserFavorite from the database, given an id

    Args: id (int)
    """

    with sqlite3.connect("./national_park.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM User_Favorites
        WHERE id = ?
        """, ( id, ))
