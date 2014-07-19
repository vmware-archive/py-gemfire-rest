from Region import *


class Repository:

    # Initializes a Repository Object
    def __init__(self, name, base_url, type):
        self.name = name
        self.base_url = base_url + name
        self.type = type
        self.region = self.get_region()

    # Deletes the specified Object from the region
    def delete(self, entities):
        if isinstance(entities, list):
            temp = ' , '.join(str(key.id) for key in entities)
            return self.region.delete(temp)
        if isinstance(entities, int):
            return self.region.delete(entities)
        else:
            return self.region.delete(entities.id)

    # Deletes all data in the region
    def delete_all(self):
        return self.region.clear()

    # Checks whether an Object with the given id exists
    def exists(self, id):
        value = self.region.get(id)
        if value is None:
            return False
        else:
            return True

    # Returns all data in the region
    def find_all(self):
        return self.region.get_all()

    # Retrieves Object(s) by the given ID(s) from the region
    def find(self, ids):
        if isinstance(ids, list):
            temp = ",".join(str(key) for key in ids)
            return self.region.get(temp)
        else:
            return self.region.get(ids)

    # Saves(s) all given Objects in the region
    def save(self, entities):
        if isinstance(entities, list):
            item = {}
            for entity in entities:
                item[entity.id] = entity
            return self.region.put_all(item)
        else:
            return self.region.put(entities.id, entities)

    # Instantiates and returns a Region object
    def get_region(self):
        return Region(self.name, self.base_url, self.type)
