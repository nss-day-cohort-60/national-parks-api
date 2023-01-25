from .wildlife_views import get_all_wildlife, get_single_wildlife_type, get_wildlife_by_park_id, create_wildlife, update_wildlife, delete_wildlife
from .natural_attractions_views import get_all_natural_attractions, get_single_natural_attraction, get_natural_attraction_by_park_id, create_natural_attraction, update_natural_attraction, delete_natural_attraction
from .amenity_views import get_all_amenities, get_all_amenity_types, get_amenity_by_id, get_amenity_type_by_id
from .park_views import get_all_parks, get_single_park
from .photo_views import get_all_photos, get_single_photo
from .blog_views import get_all_blogs, get_single_blog, get_blogs_by_user_id, get_blogs_by_park_id, create_blog, update_blog
from .user_views import get_all_users, get_user_by_id, get_user_favorite_by_id, get_all_user_favorites, create_user, create_user_favorite
