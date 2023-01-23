import sqlite3
from models import User, User_Favorite

def get_all_users():
    """fetches list of amenity types from amenities table"""
    with sqlite3.connect("./national_park.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute(
            """
        SELECT
            *
        FROM Users
        """
        )

        users = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            user = User(row["id"], row["first_name"], row["last_name"], row["email"], row["password"], row["isRanger"])

            users.append(user.__dict__)

    return users

def get_user_by_id(id):
    """fetches list of amenity types from amenities table"""
    with sqlite3.connect("./national_park.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute(
            """
        SELECT
            *
        FROM Users
        WHERE id = ?
        """, (id, )
        )

        user = {}
        row = db_cursor.fetchone()
        user = User(row["id"], row["first_name"], row["last_name"], row["email"], row["password"], row["isRanger"])

    return user.__dict__

def get_all_user_favorites():
    """fetches list of amenity types from amenities table"""
    with sqlite3.connect("./national_park.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute(
            """
        SELECT
            *
        FROM User_Favorites
        """
        )

        favorites = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            favorite = User_Favorite(row["id"], row["type_id"], row["post_id"], row["user_id"])

            favorites.append(favorite.__dict__)

    return favorites

def get_user_favorite_by_id(id):
    """fetches list of amenity types from amenities table"""
    with sqlite3.connect("./national_park.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute(
            """
        SELECT
            *
        FROM User_Favorites
        WHERE id = ?
        """, (id, )
        )

        favorite = {}
        row = db_cursor.fetchone()
        favorite = User_Favorite(row["id"], row["type_id"], row["post_id"], row["user_id"])

    return favorite.__dict__
