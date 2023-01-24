from method_mapper import method_mapper

def all(resource):
    """For GET requests to collection"""
    return method_mapper[resource]["all"]()
        
def retrieve(resource, id):
    """For GET requests to a single resource"""
    return method_mapper[resource]["single"](id)

def create(resource):
    """For POST requests to a collection"""
    return method_mapper[resource]["post"] ()

def update(resource, id):
    """For PUT requests to a single resource"""
    return method_mapper[resource]["put"](id)

def delete(resource, id):
    """For DELETE requests to a single resource"""
    return method_mapper[resource]["delete"](id)

    "wildlife": {
        "all": get_all_wildlife,
        "single": get_single_wildlife_type,
        "park_id": get_wildlife_by_park_id
    }
