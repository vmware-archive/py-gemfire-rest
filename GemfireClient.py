import requests
import jsonpickle


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
            return False

    # Lists all stored Queries in the server
    def list_all_queries(self):
        allqueries = requests.get(self.base_url + "/queries").json()
        return allqueries["queries"]

    # Instantiates and returns a Query Object
    def get_query(self, query_id):
        allqueries = requests.get(self.base_url + "/queries").json()
        queries = allqueries["queries"]
        names = [query["id"] for query in queries]
        for n in names:
            if n == query_id:
                return Query(query_id, self.base_url)
        else:
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
            return False

    # Runs an adhoc Query
    def run_query(self, query_string):
        url = self.base_url + "queries/adhoc?q=" + str(query_string)
        data = requests.get(url)
        return jsonpickle.decode(data.text)


class Region:

    # Initializes a Region Object
    def __init__(self, name, base_url):
        self.name = name
        self.base_url = base_url + name

    # Returns all the data in a Region
    def get_all(self):
        data = requests.get(self.base_url)
        fdata = jsonpickle.decode(data.text)
        return fdata[self.name]

    # Creates a new data value in the Region if the key is absent
    def create(self, key, value):
        url = self.base_url + "?key=" + str(key)
        headers = {'content-type': 'application/json'}
        jvalue = jsonpickle.encode(value)
        data = requests.post(url, data=jvalue, headers=headers)
        if data.status_code == 201:
            return True
        else:
            return False

    # Updates or inserts data for a specified key
    def put(self, key, value):
        url = self.base_url + "/" + str(key)
        headers = {'content-type': 'application/json'}
        jvalue = jsonpickle.encode(value)
        data = requests.put(url, data=jvalue, headers=headers)
        if data.status_code == 200:
            return True
        else:
            return False

    # Returns all keys in the Region
    def keys(self):
        url = self.base_url + "/keys"
        data = requests.get(url)
        fdata = jsonpickle.decode(data.text)
        return fdata["keys"]

    # Returns the data value for a specified key
    def get(self, *arg):
        sub_url = ','.join(str(key) for key in arg)
        url = self.base_url + "/" + sub_url + "?ignoreMissingKey=true"
        data = requests.get(url)
        return jsonpickle.decode(data.text)

    # Method to support region[key] notion
    def __getitem__(self, key):
        url = self.base_url + "/" + str(key) + "?ignoreMissingKey=true"
        data = requests.get(url)
        return jsonpickle.decode(data.text)

    # Insert or updates data for a multiple keys specified by a hashtable
    def put_all(self, items):
        for key in items:
            self.put(key, items[key])

    # Updates the data in a region only if the specified key is present
    def update(self, key, value):
        url = self.base_url + "/" + str(key) + "?op=REPLACE"
        headers = {'content-type': 'application/json'}
        jvalue = jsonpickle.encode(value)
        data = requests.put(url, data=jvalue, headers=headers)
        if data.status_code == 200:
            return True
        else:
            return False

    # Compares old values and if identical replaces with a new value
    def compare_and_set(self, key, value):
        url = self.base_url + "/" + str(key) + "?op=CAS"
        headers = {'content-type': 'application/json'}
        jvalue = jsonpickle.encode(value)
        data = requests.put(url, data=jvalue, headers=headers)
        if data.status_code == 200:
            return True
        else:
            return False

    # Deletes the corresponding data value for the specified key
    def delete(self, *arg):
        sub_url = ','.join(str(key) for key in arg)
        url = self.base_url + "/" + sub_url
        data = requests.delete(url)
        if data.status_code == 200:
            return True
        else:
            return False

    # Deletes all data in the Region
    def clear(self):
        data = requests.delete(self.base_url)
        if data.status_code == 200:
            return True
        else:
            return False


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
