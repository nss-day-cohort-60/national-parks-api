from views import get_all_amenities, get_all_amenity_types, get_amenity_by_id, get_amenity_type_by_id, get_all_blogs, get_single_blog, get_blogs_by_user_id, get_blogs_by_park_id, create_blog, update_blog, get_all_wildlife, get_single_wildlife_type, get_wildlife_by_park_id, create_wildlife, update_wildlife, delete_wildlife, get_all_natural_attractions, get_single_natural_attraction, get_natural_attraction_by_park_id, create_natural_attraction, update_natural_attraction, delete_natural_attraction, get_all_parks, get_all_photos, get_all_user_favorites, get_all_users, get_single_park, get_single_photo, get_user_by_id, get_user_favorite_by_id, create_user, create_user_favorite, delete_user_favorite, delete_user, delete_park_amenity, delete_amenity_type, create_park_amenity, create_amenity_type, update_user, update_park_amenity, update_amenity_type, get_photos_by_park_id, get_photos_by_user_id, create_park, create_photos, update_park, delete_park, delete_photos, update_photos

method_mapper = {
    "amenities": {
        "all": get_all_amenity_types,
        "single": get_amenity_type_by_id,
        "post": create_amenity_type,
        "put": update_amenity_type,
        "delete": delete_amenity_type
    },
    "park_amenities": {
        "all": get_all_amenities,
        "single": get_amenity_by_id,
        "post": create_park_amenity,
        "put": update_park_amenity,
        "delete": delete_park_amenity
    },
    "users": {
        "all": get_all_users,
        "single": get_user_by_id,
        "post": create_user,
        "put": update_user,
        "delete": delete_user
    },
    "user_favorites": {
        "all" : get_all_user_favorites,
        "single": get_user_favorite_by_id,
        "post": create_user_favorite,
        "put": "",
        "delete": delete_user_favorite
    },
    "blogs": {
        "all": get_all_blogs,
        "single": get_single_blog,
        "post": create_blog,
        "put": update_blog,
        "delete": ""
    },
    "wildlife": {
        "all": get_all_wildlife,
        "single": get_single_wildlife_type,
        "park_id": get_wildlife_by_park_id,
        "post": create_wildlife,
        "put": update_wildlife,
        "delete": delete_wildlife
    },
    "natural_attractions": {
        "all": get_all_natural_attractions,
        "single": get_single_natural_attraction,
        "park_id": get_natural_attraction_by_park_id,
        "post": create_natural_attraction,
        "put": update_natural_attraction,
        "delete": delete_natural_attraction
    },
    "photos": {
        "all": get_all_photos,
        "single": get_single_photo,
        "park_id": get_photos_by_park_id,
        "user_id": get_photos_by_user_id,
        "post": create_photos,
        "put": update_photos,
        "delete": delete_photos
    },
    "parks": {
        "all": get_all_parks,
        "single": get_single_park,
        "post": create_park,
        "put": update_park,
        "delete": delete_park
    },
}
