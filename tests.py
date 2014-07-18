import unittest  
from GemfireClient import *
import os


class SimpleTestCase(unittest.TestCase):
    def setUp(self):
        hostname = "mclaren.gemstone.com"
        port = 8080
        debug_mode = False
        self.client = GemfireClient(hostname, port, debug_mode)
        self.myRepo = self.client.create_repository("orders")
        self.myRegion = self.myRepo.get_region()
        
        #conn = self.client.connection()
          
    def test_list_all_regions(self):
        allregions = self.client.list_all_regions()
        print allregions
        
        #self.assertIsInstance(allregions, list)nano
        self.assertEqual(allregions[0], 'products')
        self.assertEqual(allregions[1], 'functionTest')
        self.assertEqual(allregions[2], 'orders')
        self.assertEqual(allregions[4], 'customer')
        
    def testget_region(self):
        productRegion = self.myRepo.get_region()
        print productRegion
        #self.assertNotEqual(False, productRegion)
        
    
        
    def testnew_query(self):
        random_string = os.urandom(4)
        newquery = self.client.new_query( random_string,"SELECT * FROM /orderss")
        self.assertEqual(newquery, True)
        
        
    def test_list_all_queries(self):
        allqueries = self.client.list_all_queries()
        print allqueries
        
    def test_repo(self):
        repo = self.myRepo.get_region()
        print repo
        
    def test_repo_delete(self):
        name = "abc"
        id = 001
        surname = "def"  
        self.myRepo.save(Customer(name,id,surname))
        deleted = self.myRepo.delete(001)
        print deleted
        
    def test_save(self):
        name = "abc"
        id = 002
        surname = "def"  
        saved = self.myRepo.save(Customer(name,id,surname))
        print saved
        self.myRepo.delete(002)
    
    def test_findone(self):
        name = "abc"
        id = 001
        surname = "def"  
        self.myRepo.save(Customer(name,id,surname))
        findone = self.myRepo.find(001)  
        print findone
        
    def test_findall(self):
        find = self.myRepo.find_all()
        print find
    
    def test_exists(self):
        name = "abc"
        id = 10
        surname = "def"  
        self.myRepo.save(Customer(name,id,surname))
        exists = self.myRepo.exists(10)
        print exists
        self.myRepo.delete(10)
    
    def test_delete(self):
        name = "abc"
        id = 207
        surname = "def"  
        name1 = "abc"
        id1 = 107
        surname1 = "def" 
        c1 = Customer(name1, id1, surname1)
        c2 = Customer(name, id, surname)
        c3 = [c1,c2]
        self.myRepo.save(c3)
        saved = self.myRepo.delete(107)
        print saved
        #deleted = self.myRepo.delete(c1,c2)
        #print deleted
        
    
       

    '''def testrun_query(self):
        qu = {}
        runquery = self.client.run_query('my_query2', qu)
        #self.assertIsInstance(runquery, object)'''
         
        
    def testcreate(self):
        name1 = "abc"
        id1 = 13
        surname1 = "def" 
        c1 = Customer(name1, id1, surname1)
        result = self.myRegion.create(13,c1)
        self.assertEqual(result, True)
        self.myRegion.delete(13)
        #result = self.myRegion.create(95, value)
        
            
    def testkeys(self):
        name1 = "abc"
        id1 = 78
        surname1 = "def" 
        c1 = Customer(name1, id1, surname1)
        result = self.myRegion.create(78, c1)
        self.assertEqual(result, True)
        keys = self.myRegion.keys()
        print keys
        self.myRegion.delete(78)
        
        
       
     
    def testput(self):
        name1 = "abc"
        id1 = 14
        surname1 = "def" 
        c1 = Customer(name1, id1, surname1)
        self.assertEqual(self.myRegion.put(14, c1), True)
        self.myRegion.delete(14)
        
        
        
    def testget(self): 
        name1 = "abc"
        id1 = 15
        surname1 = "def" 
        c1 = Customer(name1, id1, surname1)
        self.assertEqual(self.myRegion.put(15, c1), True)
        data = self.myRegion.get(15)
        print data
        self.myRegion.delete(15)
        #self.assertEqual(data,json)
        
    def testdirget(self):
        name1 = "abc"
        id1 = 15
        surname1 = "def" 
        c1 = Customer(name1, id1, surname1)
        self.assertEqual(self.myRegion.put(15, c1), True)
        data1 = self.myRegion[15]
        print data1
        self.assertEqual(self.myRegion.delete(15), True)
         
        
        
    def testputAll(self):  
        name1 = "abc"
        id1 = 93
        surname1 = "def" 
        c1 = Customer(name1, id1, surname1)
        name = "abc"
        id = 94
        surname = "def" 
        c2 = Customer(name, id, surname)
        item = {93:c1, 94:c2}
        self.assertEqual(self.myRegion.put_all(item), True)
        self.assertEqual(self.myRegion.delete(93,94), True)
       
        
        
    def testupdate(self):
        name1 = "abc"
        id1 = 93
        surname1 = "def" 
        c1 = Customer(name1, id1, surname1)
        name = "abc"
        id = 94
        surname = "def" 
        c2 = Customer(name, id, surname)
        item = {93:c1, 94:c2}
        
        self.assertEqual(self.myRegion.put_all(item), True)
        name3 = "abc"
        id3 = 95
        surname3 = "def" 
        c3 = Customer(name3, id3, surname3)
        updt = self.myRegion.update(94, c3)
        self.assertEqual(updt, True)
        self.assertEqual(self.myRegion.delete(93,94), True)
        
        
    def testcompareAndSet(self): 
        name1 = "abc"
        id1 = 94
        surname1 = "def" 
        c1 = Customer(name1, id1, surname1)
        name = "abc"
        id = 96
        surname = "def" 
        c2 = Customer(name, id, surname)
        self.assertEqual(self.myRegion.put(94, c1), True)
        self.assertEqual(self.myRegion.compare_and_set(94,c1,c2), True)
        self.assertEqual(self.myRegion.delete(94), True)
        
        
    def testgetAll(self):
        self.assertIsInstance(self.myRegion.get_all(), object)
    
      
    def testiterator(self):
        for key in self.myRegion.keys():
            print key
          
    def testdelete(self):
        name1 = "abc"
        id1 = 94
        surname1 = "def" 
        c1 = Customer(name1, id1, surname1)
        self.assertEqual(self.myRegion.put(94,c1), True)
        self.assertEqual(self.myRegion.delete(94), True)
        
        
    '''def testclear(self):
        clearall = self.myRegion.clear()    
        self.assertEqual(clearall, True)'''
        
    def testlistallfunctions(self):
        data = self.client.list_all_functions()
        print data
        
    def testrunfunction(self):
        value = {"args": [2]}
        
        data = self.client.execute_function("functionTest","MostValuedCustomer", value)
        print data
        
            
        
    
        

            
    
