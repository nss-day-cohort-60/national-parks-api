from views import get_all_amenities, get_all_amenity_types, get_amenity_by_id, get_amenity_type_by_id
from views import get_all_blogs, get_single_blog, get_blogs_by_user_id, get_blogs_by_park_id
from views import get_all_campgrounds, get_single_campground
from views import get_all_reservations, get_single_reservation
from views import get_all_events, get_single_event

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
        "all": get_all_events,
        "single": get_single_event,
        "post": "",
        "put": "",
        "delete": ""
    }
}

