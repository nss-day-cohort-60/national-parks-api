class Campground():
    """Creates a campground object
    """
    def __init__(self, id, name, park_id, available_sites, description):
        self.id = id
        self.name = name
        self.park_id = park_id 
        self.available_sites = available_sites
        self.description = description