import requests
import json


class GemfireClient:
    

    def createURL(self, param):
        self.url = self.base_url + param

    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port
        self.base_url = "http://" + hostname + ":" + str(port) + "/gemfire-api/v1/"

    def getAllRegionNames(self):
        data = requests.get(self.base_url).json()
        rnames = data['regions']
        names = [region['name'] for region in rnames]
        print names
        
    def listAllQueries(self):
        url = self.base_url + "/queries"
        data = requests.get(url)
        print data.text

    def getRegion(self,name):
        data = requests.get(self.base_url).json()
        rnames = data['regions']
        names = [region['name'] for region in rnames]
        for n in names:
            if n==name:
                return Region(name, self.base_url)
        else:
            print False

class Region:

   
    def __init__(self, name, base_url):
        self.name = name
        self.base_url = base_url + name
        
    def keys(self):
        url = self.base_url + "/keys"
        data = requests.get(url)
        print data.text
        
    def get(self, key):
        url = self.base_url + "/" + str(key)
        data = requests.get(url)
        print data.text
        
    #def get(self, ):
    

    


        
        
