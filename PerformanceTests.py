'''Copyright (c) [Year of Creation - Year of Last Modification]  Pivotal Software, Inc.  All Rights Reserved.
Licensed under the Apache License, Version 2.0 (the "License"); 
you may not use this file except in compliance with the License. 
You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0.
Unless required by applicable law or agreed to in writing, software distributed under the License 
is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  
See the License for the specific language governing permissions and limitations under the License.'''


from GemfireClient import *
import time
from Customer import *

class PerformanceTests:

    def __init__(self):
        hostname = raw_input("Enter hostname: ")
        port = raw_input("Enter port: ")
        self.client = GemfireClient(hostname,port)
        self.myRegion = self.client.get_region(raw_input("Enter Region Name: "))

    def warmup(self):
        for x in range(0,10):
            self.myRegion.put(x,{"random":"random"})
            self.myRegion.get(x)
        self.myRegion.clear()

    def put(self, num):
        self.warmup()
        start = time.clock()
        for x in range(0,num):
            self.myRegion.put(x,Customer("John Doe", 42))
        end = time.clock()
        return (end-start)

    def put_all(self, num):
        self.warmup()
        item = {}
        for x in range(0,num):
            item[x] = Customer("New Person", 1)
        start = time.clock()
        self.myRegion.put_all(item)
        end = time.clock()
        return (end-start)

    def get(self, num):
        self.warmup()
        for x in range(0,num):
            self.myRegion.put(x,Customer("John Doe", 42))
        start = time.clock()
        for x in range(0,num):
            self.myRegion.get(x)
        end = time.clock()
        return (end-start)

    def run_test(self,testname):
        filename = raw_input("Enter filename to store run data: ")
        file = open(filename, "w")
        op_num = input("Number of operations per run: ")
        runs = input("Number of runs: ")
        name = getattr(PerformanceTests,testname)
        total = 0
        for x in range(0,runs):
            y=name(self,op_num)
            file.write(str(y)+"\n")
            total+=y
        file.close()
        print "The average run time for " + str(op_num) + " " + testname + "s was " + str(total/runs) + " seconds"


