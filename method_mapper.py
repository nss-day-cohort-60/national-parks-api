from views import get_all_amenities, get_all_amenity_types, get_amenity_by_id, get_amenity_type_by_id, get_all_blogs, get_single_blog, get_blogs_by_user_id, get_blogs_by_park_id, create_blog, update_blog, get_all_wildlife, get_single_wildlife_type, get_wildlife_by_park_id, create_wildlife, update_wildlife, delete_wildlife, get_all_natural_attractions, get_single_natural_attraction, get_natural_attraction_by_park_id, create_natural_attraction, update_natural_attraction, delete_natural_attraction
from views import get_all_campgrounds, get_single_campground
from views import get_all_reservations, get_single_reservation
from views import get_all_events, get_single_event, get_all_registration, get_single_registration

method_mapper = {
    "amenities": {
        "all": get_all_amenities,
        "single": get_amenity_by_id,
        "post": "",
        "put": "",
        "delete": ""
    },
    "campgrounds": {
        "all": get_all_campgrounds,
        "single": get_single_campground,
        "post": "",
        "put": "",
        "delete": ""
    },
    "camping_reservations": {
        "all": get_all_reservations,
        "single": get_single_reservation,
        "post": "",
        "put": "",
        "delete": ""
    },
    "events": {
        "all": get_all_events,
        "single": get_single_event,
        "post": "",
        "put": "",
        "delete": ""
    },
    "event_registration": {
        "all": get_all_registration,
        "single": get_single_registration,
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
    }
}
