from views import get_all_amenities, get_all_amenity_types, get_amenity_by_id, get_amenity_type_by_id
from views import get_all_blogs, get_single_blog, get_blogs_by_user_id, get_blogs_by_park_id
from views import get_all_users, get_all_user_favorites, get_user_by_id, get_user_favorite_by_id

method_mapper = {
    "amenities": {
        "all": get_all_amenity_types,
        "single": get_amenity_type_by_id,
        "post": "",
        "put": "",
        "delete": ""
    },
    "park_amenities": {
        "all": get_all_amenities,
        "single": get_amenity_by_id,
        "post": "",
        "put": "",
        "delete": ""
    },
    "users": {
        "all": get_all_users,
        "single": get_user_by_id,
        "post": "",
        "put": "",
        "delete": ""
    },
    "user_favorites": {
        "all" : get_all_user_favorites,
        "single": get_user_favorite_by_id,
        "post": "",
        "put": "",
        "delete": ""
    }
}
