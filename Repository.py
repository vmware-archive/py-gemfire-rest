from Region import *


class Repository:

    # Initializes a Repository Object
    def __init__(self,name, base_url):
        self.name = name
        self.base_url = base_url + name
        self.region = self.get_region()

    def delete(self,id):
        self.region.delete(id)

    def delete_entity(self, entity):
        self.region.delete(entity.id)

    def deleteAll(self):
        self.region.clear()

    def exists(self, id):
        boolean = self.region.get(id)
        if boolean != False:
            return True
        else:
            return False

    def findAll(self):
        self.region.get_all()

    def save(self, entity):
        self.region.put(entity.id,entity)

    # Initializes and returns a Region Object
    def get_region(self):
        return Region(self.name, self.base_url)
