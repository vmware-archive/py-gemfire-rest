import requests
import jsonpickle
import logging


class Region:

    # Initializes a Region Object
    def __init__(self, name, base_url):
        self.name = name
        self.base_url = base_url + name

    # Returns all the data in a Region
    def get_all(self):
        url = self.base_url + "?ALL"
        data = requests.get(url)
        logging.debug("Sending request to " + url)
        fdata = jsonpickle.decode(data.text)
        if data.status_code == 200:
            logging.debug("Response from server: " + " ," .join(data))
            return fdata[self.name]
        else:
            self.error_response(data)

    # Creates a new data value in the Region if the key is absent
    def create(self, key, value):
        url = self.base_url + "?key=" + str(key)
        headers = {'content-type': 'application/json'}
        jvalue = jsonpickle.encode(value)
        data = requests.post(url, data=jvalue, headers=headers)
        logging.debug("Sending request to " + url)
        if data.status_code == 201:
            logging.debug("The value " + str(value) + " was created in the region for the key " + str(key))
            return True
        else:
            self.error_response(data)

    # Updates or inserts data for a specified key
    def put(self, key, value):
        url = self.base_url + "/" + str(key)
        headers = {'content-type': 'application/json'}
        jvalue = jsonpickle.encode(value)
        data = requests.put(url, data=jvalue, headers=headers)
        logging.debug("Sending request to " + url)
        if data.status_code == 200:
            logging.debug("The value " + str(value) + " was put in the region for the key " + str(key))
            return True
        else:
            self.error_response(data)

    # Returns all keys in the Region
    def keys(self):
        url = self.base_url + "/keys"
        data = requests.get(url)
        logging.debug("Sending request to " + url)
        fdata = jsonpickle.decode(data.text)
        if data.status_code == 200:
            logging.debug("Response from server: " + " ," .join(data))
            return fdata["keys"]
        else:
            self.error_response(data)

    # Returns the data value for a specified key
    def get(self, *arg):
        sub_url = ','.join(str(key) for key in arg)
        url = self.base_url + "/" + sub_url + "?ignoreMissingKey=true"
        data = requests.get(url)
        logging.debug("Sending request to " + url)
        if data.status_code == 200:
            logging.debug("Response from server: " + " ," .join(data))
            return jsonpickle.decode(data.text)
        else:
            self.error_response(data)

    # Method to support region[key] notion
    def __getitem__(self, key):
        url = self.base_url + "/" + str(key) + "?ignoreMissingKey=true"
        data = requests.get(url)
        logging.debug("Sending request to " + url)
        if data.status_code == 200:
            logging.debug("Response from server: " + " ," .join(data))
            return jsonpickle.decode(data.text)
        else:
            self.error_response(data)

    # Insert or updates data for a multiple keys specified by a hashtable
    def put_all(self, item):
        sub_url = ','.join(str(keys) for keys in item)
        url = self.base_url + "/" + sub_url
        headers = {'content-type': 'application/json'}
        jvalue = jsonpickle.encode(item.values())
        data = requests.put(url, data=jvalue, headers=headers)
        logging.debug("Sending request to " + url)
        if data.status_code == 200:
            logging.debug(str(item) + " was put into the region")
            return True
        else:
            self.error_response(data)

    # Updates the data in a region only if the specified key is present
    def update(self, key, value):
        url = self.base_url + "/" + str(key) + "?op=REPLACE"
        headers = {'content-type': 'application/json'}
        jvalue = jsonpickle.encode(value)
        data = requests.put(url, data=jvalue, headers=headers)
        logging.debug("Sending request to " + url)
        if data.status_code == 200:
            logging.debug("The value at key: " + str(key) + " was updated to " + str(value))
            return True
        else:
            self.error_response(data)

    # Compares old values and if identical replaces with a new value
    def compare_and_set(self, key, oldvalue, newvalue):
        url = self.base_url + "/" + str(key) + "?op=CAS"
        headers = {'content-type': 'application/json'}
        value = {"@old":oldvalue,"@new":newvalue}
        jvalue = jsonpickle.encode(value)
        data = requests.put(url, data=jvalue, headers=headers)
        logging.debug("Sending request to " + url)
        if data.status_code == 200:
            logging.debug(str(oldvalue) + " was replaced with " + str(newvalue) + " at the key " + str(key))
            return True
        else:
            self.error_response(data)

    # Deletes the corresponding data value for the specified key
    def delete(self, *arg):
        sub_url = ','.join(str(key) for key in arg)
        url = self.base_url + "/" + sub_url
        data = requests.delete(url)
        logging.debug("Sending request to " + url)
        if data.status_code == 200:
            logging.debug("The values for the keys: " + str(arg) + " were deleted from the region")
            return True
        else:
            self.error_response(data)

    # Deletes all data in the Region
    def clear(self):
        data = requests.delete(self.base_url)
        if data.status_code == 200:
            logging.debug("All data was cleared from the region")
            return True
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
