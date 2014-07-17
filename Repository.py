from Region import *


class Repository:

    def __init__(self,name, base_url):
        self.name = name
        self.base_url = base_url + name
        self.region = self.get_region()

    def delete(self,id):
        return self.region.delete(id)

    def delete_entities(self, objects):
        temp = ""
        temp = ' , '.join(str(key.id)for key in objects)
        print temp
        return self.region.delete(temp)
    

    def delete_all(self):
        return self.region.clear()

    def exists(self, id):
        boolean = self.region.get(id)
        if boolean != False:
            return True
        else:
            return False

    def find_all(self):
        return self.region.get_all()
        
    
    def find(self,id):
        return self.region.get(id)
    
    def find_id(self, ids):
        temp = ""
        temp = ",".join(str(key)for key in ids)
        return self.region.get(temp)

    def save(self, entity):
        return self.region.put(entity.id,entity)

    def save_all(self, entities):
        item = {}
        for entity in entities:
            item[entity.id] = entity
        return self.region.put_all(item)

    def get_region(self):
        return Region(self.name, self.base_url)
