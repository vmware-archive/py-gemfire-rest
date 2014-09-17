'''
Copyright (c) 2014 Pivotal Software, Inc.  All Rights Reserved.
Licensed under the Apache License, Version 2.0 (the "License"); 
you may not use this file except in compliance with the License. 
You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0.
Unless required by applicable law or agreed to in writing, software distributed under the License 
is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  
See the License for the specific language governing permissions and limitations under the License.
'''


import logging
import requests
import jsonpickle


class Region:

    def __init__(self, name, base_url, type):
        ''' Initializes a Region '''
        self.name = name
        self.base_url = base_url
        self.type = type

    def get_all(self):
        ''' Returns all the data in a Region '''
        url = self.base_url + "?ALL"
        data = requests.get(url)
        logging.debug("Sending request to " + url)
        fdata = jsonpickle.decode(data.text)
        if data.status_code == 200:
            logging.debug("Response from server: " + " ,".join(data))
            return fdata[self.name]
        else:
            self.error_response(data)

    def create(self, key, value):
        ''' Creates a new data value in the Region if the key is absent '''
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

    def put(self, key, value):
        ''' Updates or inserts data for a specified key '''
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

    def keys(self):
        ''' Returns all keys in the Region '''
        url = self.base_url + "/keys"
        data = requests.get(url)
        logging.debug("Sending request to " + url)
        fdata = jsonpickle.decode(data.text)
        if data.status_code == 200:
            logging.debug("Response from server: " + " ,".join(data))
            return fdata["keys"]
        else:
            self.error_response(data)

    def get(self, *arg):
        ''' Returns the data value for a specified key '''
        sub_url = ','.join(str(key) for key in arg)
        url = self.base_url + "/" + sub_url + "?ignoreMissingKey=true"
        data = requests.get(url)
        logging.debug("Sending request to " + url)
        if data.status_code == 200:
            logging.debug("Response from server: " + " ,".join(data))
            return jsonpickle.decode(data.text)
        else:
            self.error_response(data)

    def __getitem__(self, key):
        ''' Method to support region[key] notion '''
        url = self.base_url + "/" + str(key) + "?ignoreMissingKey=true"
        data = requests.get(url)
        logging.debug("Sending request to " + url)
        if data.status_code == 200:
            logging.debug("Response from server: " + " ,".join(data))
            return jsonpickle.decode(data.text)
        else:
            self.error_response(data)

    def put_all(self, item):
        ''' Insert or updates data for multiple keys specified by a hashtable '''
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

    def update(self, key, value):
        ''' Updates the data in a region only if the specified key is present '''
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

    def compare_and_set(self, key, oldvalue, newvalue):
        ''' Compares old values and if identical replaces with a new value '''
        url = self.base_url + "/" + str(key) + "?op=CAS"
        headers = {'content-type': 'application/json'}
        value = {"@old": oldvalue, "@new": newvalue}
        jvalue = jsonpickle.encode(value)
        data = requests.put(url, data=jvalue, headers=headers)
        logging.debug("Sending request to " + url)
        if data.status_code == 200:
            logging.debug(str(oldvalue) + " was replaced with " + str(newvalue) + " at the key " + str(key))
            return True
        else:
            self.error_response(data)

    def delete(self, *arg):
        ''' Deletes the corresponding data value for the specified key '''
        sub_url = ','.join(str(key) for key in arg)
        url = self.base_url + "/" + sub_url
        data = requests.delete(url)
        logging.debug("Sending request to " + url)
        if data.status_code == 200:
            logging.debug("The values for the keys: " + str(arg) + " were deleted from the region")
            return True
        else:
            self.error_response(data)

    def clear(self):
        ''' Deletes all data in the Region '''
        if self.type == "REPLICATE":
            data = requests.delete(self.base_url)
            if data.status_code == 200:
                logging.debug("All data was cleared from the region")
                return True
            else:
                self.error_response(data)
        if self.type == "PARTITION":
            keys = self.keys()
            temp = ",".join(str(key) for key in keys)
            self.delete(temp)
            return True

    def error_response(self, data):
        ''' Processes HTTP error responses '''
        if data != 400 or data != 409 or data != 405:
            logging.warning("Response from server: " + str(data.status_code) + " " + data.reason + " - " + data.text)
            print str(data.status_code) + ": " + data.reason
            return False
        else:
            logging.debug("Response from server: " + str(data.status_code) + " " + data.reason + " - " + data.text)
            return False

