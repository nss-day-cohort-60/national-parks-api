from views import get_all_amenities, get_all_amenity_types, get_amenity_by_id, get_amenity_type_by_id, get_all_blogs, get_single_blog, get_blogs_by_user_id, get_blogs_by_park_id, create_blog, update_blog, get_all_wildlife, get_single_wildlife_type, get_wildlife_by_park_id, create_wildlife, update_wildlife

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
        "put": update_wildlife    
    }
}
