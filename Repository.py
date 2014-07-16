from Region import *


class Repository:

    # Initializes a Repository Object
    def __init__(self,name, base_url):
        self.name = name
        self.base_url = base_url

    # Initializes and returns a Region Object
    def get_region(self):
        return Region(self.name, self.base_url)
