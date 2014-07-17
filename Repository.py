from Region import *


class Repository:

    def __init__(self,name, base_url):
        self.name = name
        self.base_url = base_url 
        self.region = self.get_region()

    def delete(self,id):
        self.region.delete(id)

    def delete(self, objects):
        temp = ""
        temp = ' , '.join(str(key.id)for key in objects)
        print temp
        return self.region.delete(temp)
    

    def delete_all(self):
        self.region.clear()

    def exists(self, id):
        boolean = self.region.get(id)
        if boolean != False:
            return True
        else:
            return False

    def find_all(self):
        self.region.get_all()
        
    def find_all(self, objects):
        temp = ""
        temp = ' , '.join(str(key.id)for key in objects)
        print temp
        return self.region.get(temp)

    def find(self,id):
        self.region.get(id)

    def save(self, entity):
        self.region.put(entity.id,entity)

    def save_all(self, entities):
        item = {}
        for entity in entities:
            item[entity.id] = entity
        self.region.put_all(item)

    def get_region(self):
        return Region(self.name, self.base_url)
