from GemfireClient import *
from pprint import pprint

hostname = "mclaren.gemstone.com"
port = 8080


client = GemfireClient(hostname, port)


regions = client.getAllRegionNames()
print regions[0]
print regions[1]
print regions[2]
query = client.listAllQueries()
print query[0]
print query[1]
print query[2]

print query[1][0]


myRegion = client.getRegion("orders")


ordersdata = myRegion.getAll()
print ordersdata
value = {"change":"change124"}
neworder = myRegion.create(12, value)
print neworder
putvalue = {"change":"random"}
putdata = myRegion.put(12, putvalue)
print putdata
allkeys = myRegion.keys()
print allkeys
print allkeys[1]
alldata = myRegion.get(17)
print alldata
items = {'15':{"change":"value_putall"},'17':{"change":"delete_putall"}}
putdata = myRegion.putAll(items)
print putdata
value_update = {"change":"change124"}
update = myRegion.update(17, value_update)
print update
comp_value = {"@old":{"change":"change124"}, "@new":{"change":"change"}}
compare = myRegion.compareAndSet(17, comp_value)
print compare
delet = myRegion.delete("17,18,19")
print delet



