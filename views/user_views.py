from models import User, User_Favorite
from sql_helper import get_all, get_single

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
        favorite = User_Favorite(row["id"], row["type_id"], row["post_id"], row["user_id"])

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
    favorite = User_Favorite(row["id"], row["type_id"], row["post_id"], row["user_id"])

    return favorite.__dict__
