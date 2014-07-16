from Region import *
import logging
from datetime import datetime

class GemfireClient:

    # Initializes the Client Object
    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port
        self.base_url = "http://" + hostname + ":" + str(port) + "/gemfire-api/v1/"
        logging.basicConfig(filename=(datetime.now().strftime('pyrest_%H_%M_%d_%m_%Y.log')), level=logging.DEBUG,format=('%(filename)s: ''%(levelname)s: ''%(funcName)s(): ''%(lineno)d:\t''%(message)s'))
        logging.info('Started Client')
        self.connection()

    # Checks connection to the server
    def connection(self):
        data = requests.get(self.base_url)
        if data.status_code == 200:
            logging.info("Client successfully connected to server at " + self.hostname)
            return True
        else:
            self.error_response(data)

    # Lists all names of Regions present in the server
    def list_all_regions(self):
        data = requests.get(self.base_url)
        logging.debug("Sending request to " + self.base_url)
        fdata = jsonpickle.decode(data.text)
        rnames = fdata['regions']
        names = [region['name'] for region in rnames]
        if data.status_code ==200:
            logging.debug("Response from server: " + " ,".join(data))
            return names
        else:
            self.error_response(data)

    # Initializes and returns a Region Object
    def get_region(self, name):
        data = requests.get(self.base_url).json()
        logging.debug("Sending request to " + self.base_url)
        rnames = data['regions']
        names = [region['name'] for region in rnames]
        for n in names:
            if n == name:
                logging.debug("Returned back Region object for " + name)
                return Region(name, self.base_url)
        else:
            logging.debug("Region " + name + " does not exist in the server")
            print "Region " + name + " does not exist in the server"
            return False

    # Lists all stored Queries in the server
    def list_all_queries(self):
        data = requests.get(self.base_url + "/queries")
        logging.debug("Sending request to " + self.base_url + "/queries")
        fdata = jsonpickle.decode(data.text)
        if data.status_code ==200:
            logging.debug("Response from server: " + " ," .join(data))
            return fdata["queries"]
        else:
            self.error_response(data)

    # Runs the Query with specified parameters
    def run_query(self,query_id, query_args):
        url = self.base_url + "queries/" + query_id
        headers = {'content-type': 'application/json'}
        jvalue = jsonpickle.encode(query_args)
        data = requests.post(url, data=jvalue, headers=headers)
        logging.debug("Sending request to " + url)
        if data.status_code == 200:
            logging.debug("Response from server: " + " ," .join(data))
            return jsonpickle.decode(data.text)
        else:
            self.error_response(data)

    # Creates a new Query and adds it to the server
    def new_query(self, query_id, query_string):
        url = self.base_url + "/queries?id=" + str(query_id) + "&q=" + str(query_string)
        headers = {'content-type': 'application/json'}
        jvalue = jsonpickle.encode(query_string)
        data = requests.post(url, data=jvalue, headers=headers)
        logging.debug("Sending request to " + url)
        if data.status_code == 201:
            logging.debug("Query " + query_id + " was successfully added to the server")
            return True
        else:
            self.error_response(data)

    # Runs an adhoc Query
    def adhoc_query(self, query_string):
        url = self.base_url + "queries/adhoc?q=" + str(query_string)
        data = requests.get(url)
        logging.debug("Sending request to " + url)
        if data.status_code ==200:
            logging.debug("Response from server: " + " ," .join(data))
            return jsonpickle.decode(data.text)
        else:
            self.error_response(data)

    # List all stored function ID's stored on server
    def list_all_functions(self):
        url = self.base_url + "functions"
        data = requests.get(url)
        logging.debug("Sending request to " + url)
        if data.status_code == 200:
            logging.debug("Response from server: " + " ," .join(data))
            return jsonpickle.decode(data.text)
        else:
            self.error_response(data)
    
    # Run function 
    def execute_function(self, func_id, value):
        url = self.base_url + "functions/" + str(func_id) + "?onRegion=functionTest"
        headers = {'content-type': 'application/json'}
        jvalue = jsonpickle.encode(value)
        data = requests.post(url, data=jvalue, headers=headers)
        logging.debug("Sending request to " + url)
        if data.status_code == 200:
            logging.debug("Response from server: " + " ," .join(data))
            return jsonpickle.decode(data.text)
        else:
            self.error_response(data)

    # Processes HTTP error responses
    def error_response(self,data):
        if data!=400 or data!=409 or data!=405:
            logging.warning("Response from server: " + str(data.status_code) + " " + data.reason + " - " + data.text)
            print str(data.status_code) + ": " + data.reason
            return False
        else:
            logging.debug("Response from server: " + str(data.status_code) + " " + data.reason + " - " + data.text)
            return False
        
