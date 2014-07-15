from Region import *


class GemfireClient:

    # Initializes the Client Object
    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port
        self.base_url = "http://" + hostname + ":" + str(port) + "/gemfire-api/v1/"

    # Lists all names of Regions present in the server
    def list_all_regions(self):
        data = requests.get(self.base_url).json()
        rnames = data['regions']
        names = [region['name'] for region in rnames]
        return names

    # Initializes and returns a Region Object
    def get_region(self, name):
        data = requests.get(self.base_url).json()
        rnames = data['regions']
        names = [region['name'] for region in rnames]
        for n in names:
            if n == name:
                return Region(name, self.base_url)
        else:
            print "Region " + name + " does not exist in the server"
            return False

    # Lists all stored Queries in the server
    def list_all_queries(self):
        allqueries = requests.get(self.base_url + "/queries").json()
        return allqueries["queries"]

    # Runs the Query with specified parameters
    def run_query(self,query_id, query_args):
        url = self.base_url + "queries/" + query_id
        headers = {'content-type': 'application/json'}
        jvalue = jsonpickle.encode(query_args)
        data = requests.post(url, data=jvalue, headers=headers)
        if data.status_code == 200:
            return jsonpickle.decode(data.text)
        else:
            print str(data.status_code) + ": " + data.reason
            return False

    # Creates a new Query and adds it to the server
    def new_query(self, query_id, query_string):
        url = self.base_url + "/queries?id=" + str(query_id) + "&q=" + str(query_string)
        headers = {'content-type': 'application/json'}
        jvalue = jsonpickle.encode(query_string)
        data = requests.post(url, data=jvalue, headers=headers)
        if data.status_code == 201:
            return True
        else:
            print str(data.status_code) + ": " + data.reason
            return False

    # Runs an adhoc Query
    def adhoc_query(self, query_string):
        url = self.base_url + "queries/adhoc?q=" + str(query_string)
        data = requests.get(url)
        if data.status_code ==200:
            return jsonpickle.decode(data.text)
        else:
            print str(data.status_code) + ": " + data.reason
            return False

    # List all stored function ID's stored on server
    def list_all_functions(self):
        url = self.base_url + "functions"
        data = requests.get(url)
        return jsonpickle.decode(data.text)
    
    # Run function 
    def execute_function(self, func_id, value):
        url = self.base_url + "functions/" + str(func_id) + "?onRegion=functionTest"
        headers = {'content-type': 'application/json'}
        jvalue = jsonpickle.encode(value)
        data = requests.post(url, data=jvalue, headers=headers)
        if data.status_code == 200:
            return jsonpickle.decode(data.text)
        else:
            print str(data.status_code) + ": " + data.reason
            return False
        
