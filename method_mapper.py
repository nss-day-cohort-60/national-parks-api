from views import get_all_amenities, get_all_amenity_types, get_amenity_by_id, get_amenity_type_by_id
from views import get_all_blogs, get_single_blog, get_blogs_by_user_id, get_blogs_by_park_id

method_mapper = {
    "amenities": {
        "all": get_all_amenities,
        "single": get_amenity_by_id,
        "post": "",
        "put": "",
        "delete": ""
    }
}

