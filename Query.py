import requests
import jsonpickle


class Query:

    # Initializes the Query Object
    def __init__(self, query_id, base_url):
        self.query_id = query_id
        self.base_url = base_url + "queries/" + query_id

    # Runs the Query with specified parameters
    def run(self, query_args):
        headers = {'content-type': 'application/json'}
        jvalue = jsonpickle.encode(query_args)
        data = requests.post(self.base_url, data=jvalue, headers=headers)
        return jsonpickle.decode(data.text)
