from method_mapper import method_mapper

def all(resource):
    """For GET requests to collection"""
    return method_mapper[resource]["all"]()

def retrieve(resource, id):
    """For GET requests to a single resource"""
    try: #for requests like /something?park_id=3
        parameter = list(id.keys())[0]
        value = list(id.values())[0][0]
        try: # for requests like /something?park_id=3&user_id=1
            second_parameter = list(id.keys())[1]
            second_value = list(id.values())[1][0]
            return method_mapper[resource][parameter][second_parameter](value, second_value)
        except AttributeError:
            return  method_mapper[resource][parameter](value)
    except AttributeError:
        return method_mapper[resource]["single"](id)

def create(resource, post_body):
    """For POST requests to a collection"""
    return method_mapper[resource]["post"](post_body)

def update(resource, id, post_body):
    """For PUT requests to a single resource"""
    return method_mapper[resource]["put"](id, post_body)

def delete(resource, id):
    """For DELETE requests to a single resource"""
    return method_mapper[resource]["delete"](id)
