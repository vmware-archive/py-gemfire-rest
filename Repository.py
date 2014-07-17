from Region import *
import types


class Repository:

    # Initializes a Repository Object
    def __init__(self,name, base_url):
        self.name = name
        self.base_url = base_url + name
        

    # Initializes and returns a Region Object
    def get_region(self):
        return Region(self.name, self.base_url)
    
    # Deletes the entity with the given id.
    def delete(self, id):  
        url = self.base_url + "/" + str(id)
        data = requests.delete(url)
        logging.debug("Sending request to " + url)
        if data.status_code == 200:
            logging.debug("The values for the keys: " + str(id) + " were deleted from the region")
            return True
        else:
            self.error_response(data)
    
    
    def check(self, *objects):
            return all(isinstance(object,int) for object in objects)
            
                
    # Deletes the given entities.       
    def delete(self, *objects):
            temp = []
            for key in objects:
                temp.append(str(key.id))
            sub_url = ','.join(temp)
            url = self.base_url + "/" + sub_url
            data = requests.delete(url)
            logging.debug("Sending request to " + url)
            if data.status_code == 200:
                logging.debug("The values for the keys: " + str(id) + " were deleted from the region")
                return True
            else:
                self.error_response(data)
    
    # Deletes all entities managed by the repository.
    def delete_all(self):
        data = requests.delete(self.base_url)
        if data.status_code == 200:
            logging.debug("All data was cleared from the region")
            return True
        else:
            self.error_response(data)
            
    
    # Returns whether an entity with the given id exists.        
    def exists(self, id):
        url = self.base_url + "/" + str(id) + "?ignoreMissingKey=true"
        data = requests.get(url)
        logging.debug("Sending request to " + url)
        if data.status_code == 200:
            logging.debug("Response from server: " + " ," .join(data))
            return True
        else:
            self.error_response(data)

           
    # Returns all instances of the type with the given IDs.
    def find_all(self, *arg):
        sub_url = ','.join(str(key) for key in arg)
        url = self.base_url + "/" + sub_url + "?ignoreMissingKey=true"
        data = requests.get(url)
        logging.debug("Sending request to " + url)
        if data.status_code == 200:
            logging.debug("Response from server: " + " ," .join(data))
            return jsonpickle.decode(data.content)
        else:
            self.error_response(data)
        
    # Returns all instances of the type.  
    def find_all(self):
        url = self.base_url + "?ALL"
        data = requests.get(url)
        logging.debug("Sending request to " + url)
        fdata = jsonpickle.decode(data.text)
        if data.status_code == 200:
            logging.debug("Response from server: " + " ," .join(data))
            return fdata[self.name]
        else:
            self.error_response(data)
            
    # Retrieves an entity by its id.        
    def find_one(self, id):
        url = self.base_url + "/" + str(id) + "?ignoreMissingKey=true"
        data = requests.get(url)
        logging.debug("Sending request to " + url)
        if data.status_code == 200:
            logging.debug("Response from server: " + " ," .join(data))
            return jsonpickle.decode(data.text)
        else:
            self.error_response(data)
        
        
    # Saves all given entities.   
    def save(self, objects):
        temp = []
        for key in objects:
            temp.append(str(key.id))
        sub_url = ','.join(temp)
        url = self.base_url + "/" + sub_url
        print url
        headers = {'content-type': 'application/json'}
        jvalue = jsonpickle.encode(objects)
        print jvalue
        data = requests.put(url, data=jvalue, headers=headers)
        logging.debug("Sending request to " + url)
        print data.status_code
        if data.status_code == 200:
            logging.debug("The value " + str(objects) + " was put in the region")
            return True
        else:
            return False
        
   
    def error_response(self,data):
        if data!=400 or data!=409 or data!=405:
            logging.warning("Response from server: " + str(data.status_code) + " " + data.reason + " - " + data.text)
            print str(data.status_code) + ": " + data.reason
            return False
        else:
            logging.debug("Response from server: " + str(data.status_code) + " " + data.reason + " - " + data.text)
            return False
        
    
    
    
        
   
        
    
        
       
    
