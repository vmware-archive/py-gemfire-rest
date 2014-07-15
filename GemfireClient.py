import requests
import jsonpickle
import logging

logging.basicConfig(filename='log_file.log', level=logging.DEBUG,format=('%(filename)s: '
                                '%(levelname)s: '    
                                '%(funcName)s(): '
                                '%(lineno)d:\t'
                                '%(message)s'))
logging.info('Started')


class response:
        
    def process_response(self, data):
        if data.status_code == 400: 
            logging.debug("Response from server = ")
            logging.debug(str(data.status_code) + ": " + data.reason)
            return False
        elif data.status_code == 404:
            logging.warning("Response from server = ")
            logging.warning(str(data.status_code) + ": " + data.reason)
            print str(data.status_code) + ": " + data.reason
            return False
        elif data.status_code == 500:
            logging.warning("Response from server = ")
            logging.warning(str(data.status_code) + ": " + data.reason)
            print str(data.status_code) + ": " + data.reason
            return False
        elif data.status_code == 405:
            str(data.status_code) + ": " + data.reason
            logging.debug("Response from server = ")
            logging.debug(str(data.status_code) + ": " + data.reason)
            return False
        elif data.status_code == 409:
            str(data.status_code) + ": " + data.reason
            logging.debug("Response from server = ")
            logging.debug(str(data.status_code) + ": " + data.reason)
            return False
        
        
        
class GemfireClient:

    # Initializes the Client Object
    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port
        self.base_url = "http://" + hostname + ":" + str(port) + "/gemfire-api/v1/"
        
    def connection(self):
        data = requests.get(self.base_url)
        if data.status_code == 200:
            logging.info("Connection succsessful")
            return True
        else:
            res = response()
            res.process_response(data) 
          
                
            
    def list_all_regions(self):
        data = requests.get(self.base_url).json()
        logging.debug("sending request =" + self.base_url)
        rnames = data['regions']
        logging.debug("Response from server = ")
        names = [region['name'] for region in rnames]
        logging.debug(" ," .join(names))
        return names
                 


    # Initializes and returns a Region Object
    def get_region(self, name):
        data = requests.get(self.base_url).json()
        logging.debug("sending request =" + self.base_url)
        rnames = data['regions']
        names = [region['name'] for region in rnames]
        for n in names:
            if n == name:
                logging.debug("Returned back object for region = " + name)
                return Region(name, self.base_url)
        else:
            logging.debug("Region " + name + " does not exist in the server")
            print "Region " + name + " does not exist in the server"
            return False

            
            
    # Lists all stored Queries in the server
    def list_all_queries(self):
        allqueries = requests.get(self.base_url + "/queries")
        logging.debug("sending request =" + self.base_url)
        logging.debug("Response from server = ")
        logging.debug(" ," .join(allqueries))
        return allqueries
    
           
    
    # Runs the Query with specified parameters
    def run_query(self,query_id, query_args):
        url = self.base_url + "queries/" + query_id
        logging.debug("sending request =" + url)
        headers = {'content-type': 'application/json'}
        jvalue = jsonpickle.encode(query_args)
        data = requests.post(url, data=jvalue, headers=headers)
        if data.status_code == 200:
            logging.debug("Response from server = ")
            logging.debug(str(data.status_code) + ": " + data.reason)
            return jsonpickle.decode(data.text)
        else:
            res = response()
            res.process_response(data) 
          
        

    
    # Creates a new Query and adds it to the server
    def new_query(self, query_id, query_string):
        url = self.base_url + "/queries?id=" + str(query_id) + "&q=" + str(query_string)
        logging.debug("sending request =" + url)
        headers = {'content-type': 'application/json'}
        jvalue = jsonpickle.encode(query_string)
        data = requests.post(url, data=jvalue, headers=headers)
        if data.status_code == 201:
            logging.debug("Response from server = ")
            logging.debug(str(data.status_code) + ": " + data.reason)
            return True
        else:
            res = response()
            res.process_response(data) 
          

    # Runs an adhoc Query
    def adhoc_query(self, query_string):
        url = self.base_url + "queries/adhoc?q=" + str(query_string)
        logging.debug("sending request =" + url)
        data = requests.get(url)
        if data.status_code == 200:
            logging.debug("Response from server = ")
            logging.debug(str(data.status_code) + ": " + data.reason)
            return jsonpickle.decode(data.text)
        else:
            res = response()
            res.process_response(data) 
          
    
    # List all stored function ID's stored on server
    def list_all_function(self):
        url = self.base_url + "functions"
        logging.debug("sending request =" + url)
        data = requests.get(url)
        logging.debug("Response from server = ")
        logging.debug("" .join(data))
        return jsonpickle.decode(data.text)
    
    # Run function 
    def execute_function(self, func_id, value):
        url = self.base_url + "functions/" + str(func_id) + "?onRegion=functionTest"
        logging.debug("sending request =" + url)
        headers = {'content-type': 'application/json'}
        jvalue = jsonpickle.encode(value)
        data = requests.post(url, data=jvalue, headers=headers)
        if data.status_code == 200:
            logging.debug("Response from server = ")
            logging.debug("" .join(data))
            return jsonpickle.decode(data.text)
        else:
            res = response()
            res.process_response(data) 
          


      
            

class Region:

    res = response()
    # Initializes a Region Object
    def __init__(self, name, base_url):
        self.name = name
        self.base_url = base_url + name

    # Returns all the data in a Region
    def get_all(self):
        url = self.base_url + "?ALL"
        logging.debug("sending request =" + url)
        data = requests.get(url) 
        logging.debug("Response from server = ")
        logging.debug("" .join(data))
        fdata = jsonpickle.decode(data.text)
        return fdata[self.name]

    # Creates a new data value in the Region if the key is absent
    def create(self, key, value):
        url = self.base_url + "?key=" + str(key)
        logging.debug("sending request =" + url)
        headers = {'content-type': 'application/json'}
        jvalue = jsonpickle.encode(value)
        data = requests.post(url, data=jvalue, headers=headers)
        if data.status_code == 201:
            logging.debug("Response from server = ")
            logging.debug(str(data.status_code) + ": " + data.reason)
            return True
        else:
            res = response()
            res.process_response(data) 
          
            
           
            
    # Updates or inserts data for a specified key
    def put(self, key, value):
        url = self.base_url + "/" + str(key)
        logging.debug("sending request =" + url)
        headers = {'content-type': 'application/json'}
        jvalue = jsonpickle.encode(value)
        data = requests.put(url, data=jvalue, headers=headers)
        if data.status_code == 200:
            logging.debug("Response from server = ")
            logging.debug(str(data.status_code) + ": " + data.reason)
            return True
        else:
            res = response()
            response.process_response(res, data) 

    # Returns all keys in the Region
    def keys(self):
        url = self.base_url + "/keys"
        logging.debug("sending request =" + url)
        data = requests.get(url)
        logging.debug("Response from server = ")
        logging.debug("" .join(data))
        fdata = jsonpickle.decode(data.text)
        return fdata["keys"]

    # Returns the data value for a specified key
    def get(self, *arg):
        sub_url = ','.join(str(key) for key in arg)
        url = self.base_url + "/" + sub_url + "?ignoreMissingKey=true"
        logging.debug("sending request =" + url)
        data = requests.get(url)
        if data.status_code == 200:
            logging.debug("Response from server = ")
            logging.debug("" .join(data))
            return jsonpickle.decode(data.text)
        else:
            res = response()
            response.process_response(res, data) 

    # Method to support region[key] notion
    def __getitem__(self, key):
        url = self.base_url + "/" + str(key) + "?ignoreMissingKey=true"
        logging.debug("sending request =" + url)
        data = requests.get(url)
        if data.status_code == 200:
            logging.debug("Response from server = ")
            logging.debug("" .join(data))
            return jsonpickle.decode(data.text)
        else:
            res = response()
            response.process_response(res, data) 

    # Insert or updates data for a multiple keys specified by a hashtable
    def put_all(self, item):
        sub_url = ','.join(str(keys) for keys in item)
        url = self.base_url + "/" + sub_url
        logging.debug("sending request =" + url)
        headers = {'content-type': 'application/json'}
        jvalue = jsonpickle.encode(dict.items(item))
        data = requests.put(url, data=jvalue, headers=headers) 
        if data.status_code == 200:
            logging.debug("Response from server = ")
            logging.debug(str(data.status_code) + ": " + data.reason)
            return True
        else:
            res = response()
            response.process_response(res, data) 

        
    # Updates the data in a region only if the specified key is present
    def update(self, key, value):
        url = self.base_url + "/" + str(key) + "?op=REPLACE"
        logging.debug("sending request =" + url)
        headers = {'content-type': 'application/json'}
        jvalue = jsonpickle.encode(value)
        data = requests.put(url, data=jvalue, headers=headers)
        if data.status_code == 200:
            logging.debug("Response from server = ")
            logging.debug(str(data.status_code) + ": " + data.reason)
            return True
        else:
            res = response()
            response.process_response(res, data) 
    
    # Compares old values and if identical replaces with a new value
    def compare_and_set(self, key, oldvalue, newvalue):
        url = self.base_url + "/" + str(key) + "?op=CAS"
        logging.debug("sending request =" + url)
        headers = {'content-type': 'application/json'}
        value = {"@old":oldvalue,"@new":newvalue}
        jvalue = jsonpickle.encode(value)
        data = requests.put(url, data=jvalue, headers=headers)
        if data.status_code == 200:
            logging.debug("Response from server = ")
            logging.debug(str(data.status_code) + ": " + data.reason)
            return True
        else:
            res = response()
            response.process_response(res, data) 

    # Deletes the corresponding data value for the specified key
    def delete(self, *arg):
        sub_url = ','.join(str(key) for key in arg)
        url = self.base_url + "/" + sub_url
        logging.debug("sending request =" + url)
        data = requests.delete(url)
        if data.status_code == 200:
            logging.debug("Response from server = ")
            logging.debug(str(data.status_code) + ": " + data.reason)
            return True
        else:
            res = response()
            response.process_response(res, data) 

    # Deletes all data in the Region
    def clear(self):
        data = requests.delete(self.base_url)
        logging.debug("sending request =" + self.base_url)
        if data.status_code == 200:
            logging.debug("Response from server = ")
            logging.debug(str(data.status_code) + ": " + data.reason)
            return True
        else:
            res = response()
            res.process_response(data) 
        
     
        
        


