from method_mapper import method_mapper

def all(resource):
    """For GET requests to collection"""
    return method_mapper[resource]["all"]()
        
def retrieve(resource, id):
    """For GET requests to a single resource"""
    return method_mapper[resource]["single"](id)

def create(resource, post_body):
    """For POST requests to a collection"""
    return method_mapper[resource]["post"](post_body)

def update(resource, id):
    """For PUT requests to a single resource"""
    return method_mapper[resource]["put"](id)

def delete(resource, id):
    """For DELETE requests to a single resource"""
    return method_mapper[resource]["delete"](id)