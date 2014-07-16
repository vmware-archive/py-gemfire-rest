import unittest  
from GemfireClient import *


class SimpleTestCase(unittest.TestCase):
    def setUp(self):
        hostname = "mclaren.gemstone.com"
        port = 8080
        self.client = GemfireClient(hostname, port)
        self.myRegion = self.client.get_region("products")
        
    def test_list_all_regions(self):
        allregions = self.client.list_all_regions()
        self.assertIsInstance(allregions, list)
        self.assertEqual(allregions[0], 'products')
        self.assertEqual(allregions[1], 'orders')
        self.assertEqual(allregions[2], 'customer')
        
    def testget_region(self):
        productRegion = self.client.get_region("products")
        self.assertNotEqual(False, productRegion)
        
    '''def testnewquery(self):
        newquery = self.client.newQuery("cust0018","SELECT * FROM /products WHERE id = 0018")
        self.assertEqual(newquery, True)'''
        
        
    def test_list_all_queries(self):
        allqueries = self.client.list_all_queries()
        #print allqueries
        #self.assertEqual(allqueries, dict)
        
    
    def testrun_query(self):
        runquery = self.client.run_query('SELECT * FROM /orders')
        self.assertIsInstance(runquery, object)
         
    
    def testgetQuery(self):
        query = self.client.get_query("cust0013")
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
        self.assertEqual(self.myRegion.put("108,109",items), True)
        data1 = self.myRegion[108]
        data2 = self.myRegion[109]
        self.assertEqual(self.myRegion.delete("108,109"), True)
        
        
        
        
    def testput_all(self):  
        item = {"107":{"change":"value_putall"}, "108":{"change":"delete_putall"}}
        self.myRegion.put_all(items)
        self.assertEqual(self.myRegion.put_all(item), True)
        print self.myRegion[105]
        self.assertEqual(self.myRegion.delete("107,108"), True)
        
        
    def testupdate(self):
        items = [{"abc":"cdef"},{"123":"8989"}]
        self.assertEqual(self.myRegion.put("93",items), True) 
        value_update = {"change":"random"}
        updt = self.myRegion.update(93, value_update)
        self.assertEqual(updt, True)
        #self.assertEqual(self.myRegion.get(93),'{"change":"change12400"}')
        
        
    def testcompareAndSet(self): 
        comp_value = {"@old":{"change":"random"}, "@new":{"change":"change"}}
        self.assertEqual(self.myRegion.compare_and_set(93, comp_value), True)
        
        
    def testgetAll(self):
        self.assertIsInstance(self.myRegion.get_all(), object)
        data = self.myRegion.get_all()
        #print data
    
    def testiterator(self):
        for key in self.myRegion.keys():
            print key
          
    def testdelete(self):
        items = {"change":"value_putall"} 
        self.assertEqual(self.myRegion.put("95",items), True)
        self.assertEqual(self.myRegion.delete("95"), True)
        keys = self.myRegion.keys()
        #print keys
        
    def testclear(self):
        clearall = self.myRegion.clear()    
        self.assertEqual(clearall, True)
        
        
        
   def testlistallfunctions(self):
        data = self.client.list_all_function()
        print data
        
   def testrunfunction(self):
        value = {"args": [2]}
        
        data = self.client.execute_function("MostValuedCustomer", value)
        print data
   
        
    
        

            
    
