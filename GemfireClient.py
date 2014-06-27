import requests
import json
#from main import *

class GemfireClient:
    url=""
    hostname=""
    base_url=""
    port=0

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

    def getRegion(self,name):
        data = requests.get(self.base_url).json()
        rnames = data['regions']
        names = [region['name'] for region in rnames]
        for n in names:
            if n==name:
                return Region(name)
        else:
            print "HTTP Error 500: Region Not Found"

class Region:

    name = ''
    def __init__(self, name):
        self.name = name


    

