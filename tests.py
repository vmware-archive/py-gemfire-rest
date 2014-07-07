import unittest  
from GemfireClient import *


class SimpleTestCase(unittest.TestCase):
    def setUp(self):
        hostname = "mclaren.gemstone.com"
        port = 8080
        self.client = GemfireClient(hostname, port)
        self.myRegion = self.client.getRegion("products")
        
    def testgetAllRegionNames(self):
        allregions = self.client.getAllRegionNames()
        self.assertIsInstance(allregions, list)
        self.assertEqual(allregions[0], 'products')
        self.assertEqual(allregions[1], 'orders')
        self.assertEqual(allregions[2], 'customer')
        
    def testgetRegion(self):
        productRegion = self.client.getRegion("products")
        self.assertNotEqual(False, productRegion)
        
    def testnewquery(self):
        newquery = self.client.newQuery("cust0018","SELECT * FROM /products WHERE id = 0018")
        self.assertEqual(newquery, True)
        
        
    def testlistAllQueries(self):
        allqueries = self.client.listAllQueries()
        #print allqueries
        #self.assertEqual(allqueries, dict)
        
    
    def testrunquery(self):
        runquery = self.client.runQuery('SELECT * FROM /orders')
        self.assertIsInstance(runquery, object)
         
    
    def testgetQuery(self):
        query = self.client.getQuery("cust0013")
        self.assertNotEqual(False, query)
        
    def testcreate(self):
        value = {"change":"random"}
        result = self.myRegion.create(95, value)
        self.assertEqual(result, True)
        self.myRegion.delete(95)
        
        
            
    def testkeys(self):
        value = {"change":"random"}
        result = self.myRegion.create(92, value)
        self.assertEqual(result, True)
        keys = self.myRegion.keys()
        #print keys
        self.assertEqual(keys[0], '92')
        self.myRegion.delete(92)
        
        
       
     
    def testput(self):
        putvalue = {"random":"change"}
        self.assertEqual(self.myRegion.put(93, putvalue), True)
        self.myRegion.delete(93)
        
        
        
    def testget(self): 
        putvalue = {"random":"change"}
        self.assertEqual(self.myRegion.put(96, putvalue), True)
        data = self.myRegion.get("96")
        #print data
        #self.assertEqual(data,json)
        
    def testdirget(self):
        items = [{"abc":"cdef"},{"123":"8989"}]
        self.assertEqual(self.myRegion.putAll("108,109",items), True)
        data1 = self.myRegion[108]
        data2 = self.myRegion[109]
        print data1, data2
        
        
        
        
    def testputAll(self):  
        items = [{"abc":"cdef"},{"123":"8989"}]
        self.assertEqual(self.myRegion.putAll("108,109",items), True)
        self.assertEqual(self.myRegion.delete("108,109"), True) 
        
        
    def testupdate(self): 
        value_update = {"change":"random"}
        updt = self.myRegion.update(93, value_update)
        self.assertEqual(updt, True)
        #self.assertEqual(self.myRegion.get(93),'{"change":"change12400"}')
        
    def testcompareAndSet(self): 
        comp_value = {"@old":{"change":"random"}, "@new":{"change":"change"}}
        self.assertEqual(self.myRegion.compareAndSet(93, comp_value), True)
        
        
    def testgetAll(self):
        self.assertIsInstance(self.myRegion.getAll(), object)
        data = self.myRegion.getAll()
        #print data
    
    def testiterator(self):
        for key in self.myRegion.keys():
            print key
          
    def testdelete(self):
        items = {"change":"value_putall"} 
        self.assertEqual(self.myRegion.putAll("95",items), True)
        self.assertEqual(self.myRegion.delete("95"), True)
        keys = self.myRegion.keys()
        #print keys
        
    def testclear(self):
        clearall = self.myRegion.clear()    
        self.assertEqual(clearall, True)
   
        
    
        
   
        
    
        
   
        
    
        
   
        
    
        
        

        

            
    
