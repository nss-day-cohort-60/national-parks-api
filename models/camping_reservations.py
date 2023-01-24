class Reservation():
    """Creates a campground reservation object
    """

    def __init__(self, id, start_date, end_date, campground_id, user_id):
        self.id = id
        self.start_date = start_date
        self.end_date = end_date
        self.campground_id = campground_id
        self.user_id = user_id