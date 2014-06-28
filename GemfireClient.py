import requests
import json
#from main import *

class GemfireClient:

    def createURL(self, param):
        self.url = self.base_url + param

    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port
        self.base_url= "http://" + hostname + ":" + str(port) + "/gemfire-api/v1/"

    def getAllRegionNames(self):
        data = requests.get(self.base_url).json()
        rnames = data['regions']
        names = [region['name'] for region in rnames]
        print names

    def getRegion(self,name):
        data = requests.get(self.base_url).json()
        rnames = data['regions']
        names = [region['name'] for region in rnames]
        for n in names:
            if n==name:
                return Region(name,self.base_url)
        else:
            print False

class Region:

    def __init__(self, name, base_url):
        self.name = name
        self.base_url = base_url + name

    def getAll(self):
        data = requests.get(self.base_url)
        print data.text

    def keys(self):
        url = self.base_url + "/keys"
        data = requests.get(url)
        print data.text
        
    def get(self, key):
        url = self.base_url + "/" + str(key)
        data = requests.get(url)
        print data.text
        
    def create(self, key, value):
        url = self.base_url + "?key=" + str(key)
        headers = {'content-type': 'application/json'}
        r = requests.post(url, data=json.dumps(value), headers=headers)
        if r.status_code == 201 or r.status_code == 202:
            print True
        else:
            print False

    def put(self,key,value):
        url = self.base_url + "/" + str(key)
        headers = {'content-type': 'application/json'}
        r = requests.put(url, data=json.dumps(value), headers=headers)
        if r.status_code == 200:
            print True
        else:
            print False





