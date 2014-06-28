from GemfireClient import *

hostname = "mclaren.gemstone.com"
port = 8080
client = GemfireClient(hostname, port)
data = requests.get(client.base_url).json()


client.getAllRegionNames()
client.listAllQueries()
myRegion = client.getRegion("orders")
myRegion.keys()
myRegion.get("2")




