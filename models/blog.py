class Blog():
    """Model for blog dictionaries"""
    def __init__(self, id, title, post_body, date_created, user_id="", park_id=""):
        self.id = id
        self.title = title
        self.post_body = post_body
        self.date_created = date_created
        self.user_id = user_id
        self.park_id = park_id
