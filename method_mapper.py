from views import get_all_amenities, get_all_amenity_types, get_amenity_by_id, get_amenity_type_by_id, get_all_blogs, get_single_blog, get_blogs_by_user_id, get_blogs_by_park_id, create_blog, update_blog, get_all_wildlife, get_single_wildlife_type, get_wildlife_by_park_id, create_wildlife, update_wildlife, delete_wildlife, get_all_natural_attractions, get_single_natural_attraction, get_natural_attraction_by_park_id, create_natural_attraction, update_natural_attraction, delete_natural_attraction, get_single_park, get_all_parks, get_all_photos, get_photos_by_park_id, get_photos_by_user_id, get_single_photo, create_photos

method_mapper = {
    "amenities": {
        "all": get_all_amenities,
        "single": get_amenity_by_id,
        "post": "",
        "put": "",
        "delete": ""
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
        "put": "",
        "delete": ""
    },
    "parks": {
        "all": get_all_parks,
        "single": get_single_park,
        "post": create_photos,
        "put": "",
        "delete": ""
    },
}
