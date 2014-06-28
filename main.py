from GemfireClient import *

hostname = "mclaren.gemstone.com"
port = 8080
client = GemfireClient(hostname, port)
data = requests.get(client.base_url).json()
#print data


client.getAllRegionNames()
orderRegion = client.getRegion("orders")
value = {"change":"change"}
orderRegion.put(9,value)
