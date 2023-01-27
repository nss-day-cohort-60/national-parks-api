class ParkAmenity():
    """defines ParkAmenity Class"""
    def __init__(self, id, name, amenity_id, park_id, type= None):
        self.id = id
        self.name = name
        self.type= type
        self.amenity_id = amenity_id
        self.park_id = park_id
