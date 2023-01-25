from views import get_all_amenities, get_all_amenity_types, get_amenity_by_id, get_amenity_type_by_id, get_all_blogs, get_single_blog, get_blogs_by_user_id, get_blogs_by_park_id, create_blog, update_blog, get_all_wildlife, get_single_wildlife_type, get_wildlife_by_park_id, create_wildlife, update_wildlife, delete_wildlife, get_all_natural_attractions, get_single_natural_attraction, get_natural_attraction_by_park_id, create_natural_attraction, update_natural_attraction, delete_natural_attraction, get_all_campgrounds, get_single_campground, get_all_reservations, get_single_reservation, get_all_events, get_single_event, get_all_registration, get_single_registration, create_campground, delete_campground, update_campground, create_reservation, update_reservation, delete_reservation, update_event_registration, create_event_registration, delete_event_registration, create_event, update_event, delete_event

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
        "post": create_campground,
        "put": update_campground,
        "delete": delete_campground
    },
    "camping_reservations": {
        "all": get_all_reservations,
        "single": get_single_reservation,
        "post": create_reservation,
        "put": update_reservation,
        "delete": delete_reservation
    },
    "events": {
        "all": get_all_events,
        "single": get_single_event,
        "post": create_event,
        "put": update_event,
        "delete": delete_event
    },
    "event_registration": {
        "all": get_all_registration,
        "single": get_single_registration,
        "post": create_event_registration,
        "put": update_event_registration,
        "delete": delete_event_registration
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
