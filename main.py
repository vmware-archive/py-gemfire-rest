from GemfireClient import *

hostname = "mclaren.gemstone.com"
port = 8080
client = GemfireClient(hostname, port)


client.listAllQueries()
client.runQuery("SELECT * FROM /customer c WHERE c.customerId = 1012")

client.getAllRegionNames()
client.newQuery("orderselect", "SELECT * FROM /orders")


myRegion = client.getRegion("customer")
myquery =  client.AllQueries("selectOrders")
value = {"@old":{"change":"change124"}, "@new":{"change":"change"}}
items = {12:{"change":"value"},13:{"change":"delete"}}
myRegion.put(10,value)
myRegion.getAll()
client.runQuery("SELECT * FROM /customer")
myRegion.keys()
myRegion.get("9")
myRegion.get("2,3,4,5")
myRegion.putAll(items)
myRegion.put(14, value)
myRegion.update(14, value)
myRegion.delete("13,14")
myRegion.compareAndSet(9,value)











