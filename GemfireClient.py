import requests
import json
from pprint import pprint

class GemfireClient:

    #Initializes the Client Object
    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port
        self.base_url= "http://" + hostname + ":" + str(port) + "/gemfire-api/v1/"

    #Lists all names of Regions present in the server
    def getAllRegionNames(self):
        data = requests.get(self.base_url).json()
        rnames = data['regions']
        names = [region['name'] for region in rnames]
        print names

    #Initializes and returns a Region Object
    def getRegion(self,name):
        data = requests.get(self.base_url).json()
        rnames = data['regions']
        names = [region['name'] for region in rnames]
        for n in names:
            if n==name:
                return Region(name,self.base_url)
        else:
            print False

    #Lists all stored Queries in the server
    def listAllQueries(self):
        allqueries = requests.get(self.base_url+"/queries").json()
        pprint(allqueries)

    #Instantiates and returns a Query Object
    def getQuery(self,queryID):
        allqueries = requests.get(self.base_url+"/queries").json()
        queries = allqueries["queries"]
        names = [query["id"] for query in queries]
        for n in names:
            if n==queryID:
                return Query(queryID,self.base_url)
        else:
            print False

    #Creates a new Query and adds it to the server
    def newQuery(self, Query_id, Query_string):
        url = self.base_url + "/queries?id=" + str(Query_id) + "&q=" + str(Query_string)
        headers = {'content-type': 'application/json'}
        data = requests.post(url, data=json.dumps(Query_string), headers=headers)
        if data.status_code == 201:
            print True
        else:
            print False

    #Runs an adhoc Query
    def runQuery(self,Query_string):
        url = self.base_url + "queries/adhoc?q=" + str(Query_string)
        data = requests.get(url)
        print data.text
        if data.status_code == 200:
            print True
        else:
            print False


class Region:

    #Initializes a Region Object
    def __init__(self, name, base_url):
        self.name = name
        self.base_url = base_url + name

    #Returns all the data in a Region
    def getAll(self):
        data = requests.get(self.base_url)
        print data.text

    #Creates a new data value in the Region if the key is absent
    def create(self, key, value):
        url = self.base_url + "?key=" + str(key)
        headers = {'content-type': 'application/json'}
        data = requests.post(url, data=json.dumps(value), headers=headers)
        if data.status_code == 201:
            print True
        else:
            print False

    #Updates or inserts data for a specified key
    def put(self,key,value):
        url = self.base_url + "/" + str(key)
        headers = {'content-type': 'application/json'}
        data = requests.put(url, data=json.dumps(value), headers=headers)
        if data.status_code == 200:
            print True
        else:
            print False

    #Returns all keys in the Region
    def keys(self):
        url = self.base_url + "/keys"
        data = requests.get(url)
        print data.text

    #Returns the data value for a specified key
    def get(self, key):
        url = self.base_url + "/" + str(key) +"?ignoreMissingKey=true"
        data = requests.get(url)
        print data.text

    #Insert or updates data for a multiple keys specified by a hashtable
    def putAll(self,items):
        for key in items:
            self.put(key,items[key])

    #Updates the data in a region only if the specified key is present
    def update(self,key,value):
        url = self.base_url + "/" + str(key) +"?op=REPLACE"
        headers = {'content-type': 'application/json'}
        data = requests.put(url, data=json.dumps(value), headers=headers)
        if data.status_code == 200:
            print True
        else:
            print False
            
    #Compares old values and if identical replaces with a new value
    def compareAndSet(self,key,value):
        url = self.base_url + "/" + str(key) +"?op=CAS"
        headers = {'content-type': 'application/json'}
        data = requests.put(url, data=json.dumps(value), headers=headers)
        if data.status_code == 200:
            print True
        else:
            print False

    #Deletes the corresponding data value for the specified key
    def delete(self,key):
        url = self.base_url + "/" + str(key)
        data = requests.delete(url)
        if data.status_code == 200:
            print True
        else:
            print False

    #Deletes all data in the Region
    def clear(self):
        data = requests.delete(self.base_url)
        if data.status_code == 200:
            print True
        else:
            print False


class Query:

    #Initializes the Query Object
    def __init__(self, queryID, base_url):
        self.queryID = queryID
        self.base_url = base_url + "queries/" + queryID

    #Runs the Query with specified parameters
    def run(self,Query_args):
        headers = {'content-type': 'application/json'}
        data = requests.post(self.base_url, data=json.dumps(Query_args), headers=headers)
        print data.text
        if data.status_code == 200:
            print True
        else:
            print False
