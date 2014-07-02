import unittest  
from GemfireClient import *


class SimpleTestCase(unittest.TestCase):
    def setUp(self):
        hostname = "mclaren.gemstone.com"
        port = 8080
        self.client = GemfireClient(hostname, port)
        self.myRegion = self.client.getRegion("orders")
        
    def testgetAllRegionNames(self):
        allregions = self.client.getAllRegionNames()
        self.assertEqual(allregions[0], 'customer')
        self.assertEqual(allregions[1], 'products')
        self.assertEqual(allregions[2], 'orders')
        
    def testgetRegion(self):
        region = self.client.getRegion("orders")
        self.assertNotEqual(False, region)
        
    def testlistAllQueries(self):
        allqueries = self.client.listAllQueries()
        self.assertEqual(allqueries[0], 'SELECT o FROM /orders o WHERE o.quantity > $1 AND o.totalprice > $2')
        
    def testnewquery(self):
        newquery = self.client.newQuery('custproducts','SELECT * FROM /products')
        self.assertEqual(newquery, True) 
        
    def testrunquery(self):
        runquery = self.client.runQuery('SELECT * FROM /orders')
        self.assertEqual(runquery, True) 
         
    
    def testgetQuery(self):
        query = self.client.getQuery("selectOrders")
        self.assertNotEqual(False, query)
        
    def testkeys(self):
        keys = self.myRegion.keys()
        self.assertEqual(keys[0], '1000') 
        self.assertEqual(keys[1], '1001') 
        
    
              
    def testcreate(self):
        value = {"change":"chan"}
        self.assertEqual(self.myRegion.create(30, value), True)
        
    
    def testput(self):
        putvalue = {"random":"randomggg"}
        self.assertEqual(self.myRegion.put(24, putvalue), True)   
        
        
    def testputAll(self):  
        items = {'15':{"change":"value_putall"},'17':{"change":"delete_putall"}}
        self.assertEqual(self.myRegion.putAll(items), True)
        
        
    def testupdate(self): 
        value_update = {"change":"change12400"}
        self.assertEqual(self.myRegion.update(1, value_update), True)
         
        
    def testcompareAndSet(self): 
        comp_value = {"@old":{"change":"change12400"}, "@new":{"change":"change"}}
        self.assertEqual(self.myRegion.compareAndSet(17, comp_value), True)
        
    def testdelete(self):
        self.assertEqual(self.myRegion.delete("20"), True)   
        
   
        
    
        
   
        
    
        
        

        

            
    
