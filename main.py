from GemfireClient import *

hostname = "mclaren.gemstone.com"
port = 8080
client = GemfireClient(hostname, port)
data = requests.get(client.base_url).json()


myRegion = client.getRegion("orders")
value = {"change":"change"}
myRegion.put(9,value)
myRegion.getAll()

myRegion.keys()
myRegion.get("2")







