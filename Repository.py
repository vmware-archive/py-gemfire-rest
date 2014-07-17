from Region import *


class Repository:

    def __init__(self,name, base_url,type):
        self.name = name
        self.base_url = base_url + name
        self.type = type
        self.region = self.get_region()

    def delete(self, objects):
        if type(objects) is list:
            temp = ""
            temp = ' , '.join(str(key.id)for key in objects)
            return self.region.delete(temp)
        else:
            return self.region.delete(objects)
    

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
    
    
    def find(self, ids):
        if type(ids) is list:
            temp = ""
            temp = ",".join(str(key)for key in ids)
            print temp
            return self.region.get(temp)
        else:
            return self.region.get(ids)

    def save(self, entities):
        if type(entities) is list:
            item = {}
            for entity in entities:
                item[entity.id] = entity
                return self.region.put_all(item)
        else:
            return self.region.put(entities.id,entities)

    def get_region(self):
        return Region(self.name, self.base_url, self.type)
