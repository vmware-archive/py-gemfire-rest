
m GemfireClient import *

hostname = "mclaren.gemstone.com"
port = 8080
client = GemfireClient(hostname, port)
data = requests.get(client.base_url).json()



c = GemfireClient(hostname, port)
client.getAllRegionNames()
customerRegion = client.getRegion("orders")
