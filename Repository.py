from Region import *


class Repository:

    # Initializes a Repository Object
    def __init__(self,name, base_url):
        self.name = name
        self.base_url = base_url + name
        

    # Initializes and returns a Region Object
    def get_region(self):
        return Region(self.name, self.base_url)
    
    def delete(self, id):  
        url = self.base_url + "/" + str(id)
        data = requests.delete(url)
        logging.debug("Sending request to " + url)
        if data.status_code == 200:
            logging.debug("The values for the keys: " + str(id) + " were deleted from the region")
            return "deleted"
        else:
            return False
        
    def delete_all(self):
        data = requests.delete(self.base_url)
        if data.status_code == 200:
            logging.debug("All data was cleared from the region")
            return True
        else:
            self.error_response(data)
            
    def delete(self, object):  
        url = self.base_url + "/" + str(object.id)
        data = requests.delete(url)
        logging.debug("Sending request to " + url)
        if data.status_code == 200:
            logging.debug("The values for the keys: " + str(id) + " were deleted from the region")
            return "deleted"
        else:
            return False
            
    def exists(self, id):
        url = self.base_url + "/" + str(id) + "?ignoreMissingKey=true"
        data = requests.get(url)
        logging.debug("Sending request to " + url)
        if data.status_code == 200:
            logging.debug("Response from server: " + " ," .join(data))
            return True
        else:
            return False
    
   
    def find_one(self, id):
        url = self.base_url + "/" + str(id) + "?ignoreMissingKey=true"
        data = requests.get(url)
        logging.debug("Sending request to " + url)
        if data.status_code == 200:
            logging.debug("Response from server: " + " ," .join(data))
            return jsonpickle.decode(data.text)
        else:
            return False
            
   
    def find_all(self, *arg):
        sub_url = ','.join(str(key) for key in arg)
        url = self.base_url + "/" + sub_url + "?ignoreMissingKey=true"
        data = requests.get(url)
        logging.debug("Sending request to " + url)
        if data.status_code == 200:
            logging.debug("Response from server: " + " ," .join(data))
            return jsonpickle.decode(data.content)
        else:
            return False
        
    def find_all(self, *arg):
        url = self.base_url + "?ALL"
        data = requests.get(url)
        logging.debug("Sending request to " + url)
        fdata = jsonpickle.decode(data.text)
        if data.status_code == 200:
            logging.debug("Response from server: " + " ," .join(data))
            return fdata[self.name]
        else:
            self.error_response(data)
        
        
    
    def save(self, object):  
        url = self.base_url + "/" + str(object.id)
        headers = {'content-type': 'application/json'}
        jvalue = jsonpickle.encode(object)
        data = requests.put(url, data=jvalue, headers=headers)
        logging.debug("Sending request to " + url)
        if data.status_code == 200:
            logging.debug("The value " + str(object) + " was put in the region for the key " + str(object.id))
            return True
        else:
            return False
    
        
    
    
        
   
        
    
        
       
    
