import requests
import json
from pprint import pprint


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
        pprint(names)

    def getRegion(self,name):
        data = requests.get(self.base_url).json()
        rnames = data['regions']
        names = [region['name'] for region in rnames]
        for n in names:
            if n==name:
                return Region(name,self.base_url)
        else:
            print False
            
    def listAllQueries(self):
        allqueries = requests.get(self.base_url+"/queries").json()
        pprint(allqueries)

    def newQuery(self, Query_id, Query_string):
        url = self.base_url + "/queries?id=" + str(Query_id) + "&q=" + str(Query_string)
        headers = {'content-type': 'application/json'}
        r = requests.post(url, data=json.dumps(Query_string), headers=headers) 
        if r.status_code == 201 or r.status_code == 202:
            print True
        else:
            print False
            
    def run(self,Query_id, Query_args):
        url = self.base_url + "/queries/" + str(Query_id)
        headers = {'content-type': 'application/json'}
        r = requests.post(url, data=json.dumps(Query_args), headers=headers)
        print r.status_code 
        if r.status_code == 201 or r.status_code == 202:
            print True
        else:
            print False
            
        
        
        
class Region:

    def __init__(self, name, base_url):
        self.name = name
        self.base_url = base_url + name

    def getAll(self):
        data = requests.get(self.base_url)
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

    def keys(self):
        url = self.base_url + "/keys"
        data = requests.get(url)
        print data.text
        
    def get(self, key):
        url = self.base_url + "/" + str(key) +"?ignoreMissingKey=true"
        data = requests.get(url)
        print data.text
        
    
   
    def putAll(self,items):
        for key in items:
            self.put(key,items[key]) 
            
    
    def update(self,key,value):
        url = self.base_url + "/" + str(key) +"?op=REPLACE"
        headers = {'content-type': 'application/json'}
        r = requests.put(url, data=json.dumps(value), headers=headers)
        if r.status_code == 200:
            print True
        else:
            print False
                          
    def delete(self,key):
        url = self.base_url + "/" + str(key)
        r = requests.delete(url)
        if r.status_code == 200:
            print True
        else:
            print False
            
            
#class Query:
    
    #def run(self):
    
    
        
    


        
        
