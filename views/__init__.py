from .wildlife_views import get_all_wildlife, get_single_wildlife_type, get_wildlife_by_park_id, create_wildlife, update_wildlife, delete_wildlife
from .natural_attractions_views import get_all_natural_attractions, get_single_natural_attraction, get_natural_attraction_by_park_id, create_natural_attraction, update_natural_attraction, delete_natural_attraction
from .blog_views import get_all_blogs, get_single_blog, get_blogs_by_user_id, get_blogs_by_park_id, create_blog, update_blog, delete_blog, get_blogs_by_park_id_and_search_term, get_blogs_by_search_term
from .photo_views import get_all_photos, get_photos_by_park_id, get_photos_by_user_id, get_single_photo, create_photos, delete_photos, update_photos, get_photos_by_user_id_and_park_id
from .park_views import get_all_parks, get_single_park, create_park, delete_park, update_park
from .amenity_views import get_all_amenities, get_all_amenity_types, get_amenity_by_id, get_amenity_type_by_id, delete_amenity_type, delete_park_amenity, create_amenity_type, create_park_amenity, update_amenity_type, update_park_amenity, get_amenities_by_park_id
from .campground_requests import get_all_campgrounds, get_single_campground, create_campground, delete_campground, update_campground, get_campgrounds_by_park
from .campground_reservation_requests import get_all_reservations, get_single_reservation, create_reservation, update_reservation, delete_reservation
from .event_requests import get_all_events, get_single_event, create_event, update_event, delete_event
from .event_registration_requests import get_all_registration, get_single_registration, update_event_registration, create_event_registration, delete_event_registration
from .user_views import get_all_users, get_user_by_id, get_user_favorite_by_id, get_all_user_favorites, create_user, create_user_favorite, delete_user_favorite, delete_user, update_user, get_user_by_email
