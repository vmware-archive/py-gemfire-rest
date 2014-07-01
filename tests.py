import unittest  
from GemfireClient import *


class SimpleTestCase(unittest.TestCase):
    def setUp(self):
        hostname = "mclaren.gemstone.com"
        port = 8080
        self.client = GemfireClient(hostname, port)
        self.myRegion = self.client.getRegion("orders")
        
     
    def testgetRegion(self):
        region = self.client.getRegion("orders")
        self.assertNotEqual(False, region)
         
    
    def testgetQuery(self):
        query = self.client.getQuery("selectOrders")
        self.assertNotEqual(False, query)
              
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
        

            
    
