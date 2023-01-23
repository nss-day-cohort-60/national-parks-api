class Event():
    """Creates an event object
    """

    def __init__(self, id, name, description, start_date, park_id):
        self.id = id
        self.name = name
        self.description = description
        self.start_date = start_date
        self.park_id = park_id