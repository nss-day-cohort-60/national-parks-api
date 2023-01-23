from urllib.parse import urlparse, parse_qs
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from views import get_all_wildlife, get_single_wildlife_type, get_wildlife_by_park_id, get_all_natural_attractions, get_single_natural_attraction


get_method_mapper = {
    'wildlife': {"single": get_single_wildlife_type, "all": get_all_wildlife, "park_id": get_wildlife_by_park_id},
    'natural_attractions': {"single": get_single_natural_attraction, "all": get_all_natural_attractions},
    # 'customers': {"single": get_single_customer, "all": get_all_customers, "email": get_customer_by_email},
    # 'employees': {"single": get_single_employee, "all": get_all_employees, 'location_id': get_employee_by_location_id},
}

# post_method_mapper = {
#     'animals': {"required_keys": ["name", "breed", "status", "location_id", "customer_id"], "creation_method": create_animal},
#     'locations': {"required_keys": ["name", "address"], "creation_method": create_location},
#     'customers': {"required_keys": ["name", "address", "email", "password"], "creation_method": create_customer},
#     'employees':  {"required_keys": ["name", "address", "location_id"], "creation_method": create_employee}
# }

# delete_method_mapper = {
#     'animals': delete_animal,
#     'locations': delete_location,
#     'customers': delete_customer,
#     'employees':  delete_employee
# }

# put_method_mapper = {
#     'animals': update_animal,
#     'locations': update_location,
#     'customers': update_customer,
#     'employees': update_employee
# }


class HandleRequests(BaseHTTPRequestHandler):
    # This is a Docstring it should be at the beginning of all classes and functions
    # It gives a description of the class or function
    """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
    """

    # Here's a class function

    def parse_url(self, path):
        """Parse the url into the resource and id"""
        parsed_url = urlparse(path)
        path_params = parsed_url.path.split('/')  # ['', 'animals', 1]
        resource = path_params[1]

        if parsed_url.query:
            query = parse_qs(parsed_url.query)
            return (resource, query)

        pk = None
        try:
            pk = int(path_params[2])
        except (IndexError, ValueError):
            pass
        return (resource, pk)

    def all(self, resource):
        self._set_headers(200)
        response = get_method_mapper[resource]["all"]()
        return response

    def retrieve(self):
        response = None
        if '?' not in self.path:
            (resource, id) = self.parse_url(self.path)
            response = self.get_single_by_id(resource, id)
        else:
            (resource, query) = self.parse_url(self.path)
            param = list(query.keys())[0]
            val = list(query.values())[0][0]
            response = self.get_single_by_keyword(resource, param, val)
        return response

    def get_single_by_id(self, resource, id):

        response = None

        if get_method_mapper.get(resource):
            response = get_method_mapper[resource]["single"](id)

        if response:
            self._set_headers(200)
        else:
            response = self.create_error_message(
                404, f'No animal with id={id} found')

        return response

    def get_single_by_keyword(self, resource, param, val):
        if get_method_mapper.get(resource).get(param):
            response = get_method_mapper[resource][param](val)
            if len(response) > 0:
                self._set_headers(200)
            else:
                response = self.create_error_message(404, 'No animals found')
        else:
            response = self.create_error_message(404, 'Invalid query params')
        return response

    def create_error_message(self, header=404, msg="Invalid input", ):
        self._set_headers(header)
        response = {"message": msg}
        return response

    def create(self, resource, post_body):
        response = None
        if not post_method_mapper.get(resource):
            response = self.create_error_message(
                404, f'resource {resource} not found')
            return response

        required_keys = post_method_mapper[resource]['required_keys']
        post_body_keys = post_body.keys()
        missing_keys = [x for x in required_keys if x not in post_body_keys]
        extra_keys = [x for x in post_body_keys if x not in required_keys]

        if missing_keys:
            response = self.create_error_message(
                400, "Missing properties: "+", ".join(missing_keys))
            return response
        if extra_keys:
            response = self.create_error_message(
                400, "Invalid properties: "+", ".join(extra_keys))
            return response

        self._set_headers(200)
        response = post_method_mapper[resource]['creation_method'](post_body)
        return response

    def update(self, resource, id, put_body):
        response = None
        required_keys = post_method_mapper[resource]['required_keys']
        put_body_keys = put_body.keys()
        missing_keys = [x for x in required_keys if x not in put_body_keys]
        extra_keys = [x for x in put_body_keys if x not in required_keys]

        if missing_keys:
            response = self.create_error_message(
                400, "Missing params: "+", ".join(missing_keys))
            return response
        if extra_keys:
            response = self.create_error_message(
                400, "Invalid params: "+", ".join(extra_keys))
            return response

        response = put_method_mapper[resource](id, put_body)
        return response

    def delete(self, resource, id):
        delete_method_mapper[resource](id)
        self._set_headers(204)

    # Here's a method on the class that overrides the parent's method.
    # It handles any GET request.

    def do_GET(self):
        """Handles GET requests to the server...responds to the client's GET request
        """
        (resource, id) = self.parse_url(self.path)
        if not get_method_mapper.get(resource):
            response = self.create_error_message(
                400, f'invalid resource {resource}')
            self.wfile.write(json.dumps(response).encode())
            return

        if id is None:
            response = self.all(resource)
        else:
            response = self.retrieve()

        self.wfile.write(json.dumps(response).encode())

    # Here's a method on the class that overrides the parent's method.
    # It handles any POST request.

    def do_POST(self):
        """Handles POST requests to the server """

        (resource, id) = self.parse_url(self.path)
        if not post_method_mapper.get(resource):
            response = self.create_error_message(
                400, f'invalid resource {resource}')
            self.wfile.write(json.dumps(response).encode())
            return

        content_len = int(self.headers.get('content-length', 0))
        if content_len == 0:
            response = self.create_error_message(
                404, "Post request must have a body")
            self.wfile.write(json.dumps(response).encode())
            return

        content = self.rfile.read(content_len)
        # Convert JSON string to a Python dictionary
        post_body = json.loads(content)

        response = self.create(resource, post_body)
        self.wfile.write(json.dumps(response).encode())

    def do_DELETE(self):
        """method to process the DELETE request. Uses response code 204: request processed, no information to send back/don't need to refresh"""

        # Parse the URL
        (resource, id) = self.parse_url(self.path)
        response = None
        if not delete_method_mapper.get(resource):
            response = self.create_error_message(
                400, f'invalid resource {resource}')
            self.wfile.write(json.dumps(response).encode())
            return
        self.delete(resource, id)

    # A method that handles any PUT request.

    def do_PUT(self):
        (resource, id) = self.parse_url(self.path)
        if not put_method_mapper.get(resource):
            response = self.create_error_message(
                400, f'invalid resource {resource}')
            self.wfile.write(json.dumps(response).encode())
            return

        content_len = int(self.headers.get('content-length', 0))
        if content_len == 0:
            response = self.create_error_message(
                404, "Post request must have a body")
            self.wfile.write(json.dumps(response).encode())
            return

        content = self.rfile.read(content_len)
        # Convert JSON string to a Python dictionary
        put_body = json.loads(content)

        response = self.update(resource, id, put_body)

        if not response:
            response = self.create_error_message(
                400, f'update failed for resource={resource} id= {id}')
        else:
            self._set_headers(200)
        self.wfile.write(json.dumps(response).encode())

    def _set_headers(self, status):
        # Notice this Docstring also includes information about the arguments passed to the function
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    # Another method! This supports requests with the OPTIONS verb.
    def do_OPTIONS(self):
        """Sets the options headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                         'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                         'X-Requested-With, Content-Type, Accept')
        self.end_headers()


# This function is not inside the class. It is the starting
# point of this application.
def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    print("Server running on port ", port)
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
