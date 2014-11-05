# py-gemfire-rest
=================

This library enables your python applications to use GemFire as a datastore. (GemFire is a distributed key-value store. A short tutorial can be found at http://goo.gl/rF93fn). This library exposes Spring's CrudRepository like methods in an effort to simplify GemFire's APIs while still giving access to advanced GemFire features (details below). 

## Installation
---------------

Using pip installation is simple
```
    $ sudo pip install gemfire-rest
```
or from source:
```
    $ sudo python setup.py install
```
## Quick Start
--------------

1. Start the GemFire REST service by [following the instructions](http://gemfire.docs.pivotal.io/latest/userguide/index.html#gemfire_rest/setup_config.html)
2. Create a Region on the server (Region is a distributed ConcurrentMap in which GemFire stores the data). 
```
    gfsh>create region --name=orders --type=PARTITION
```
3. 
```python
    >>> from gemfire *
    >>> client = GemfireClient(hostname="localhost", port=8080)
    >>> myRepo = client.create_repository("orders")
    >>> myRepo.save(order)
```

where the order object has an "id" instance variable. The library handles converting the object to/from json. 

## API Reference
----------------

This library exercises [GemFire's REST APIs](http://gemfire.docs.pivotal.io/latest/userguide/index.html#gemfire_rest/book_intro.html) for enabling your python application to use GemFire as its datastore. To get started, we create a client by providing a hostname and port for an already running endpoint. 
```python
    client = GemfireClient(hostname="localhost", port=8080)
```

For each type of Object that we want to store in GemFire, we create a repository (Please not that you will have to create a Region on the server with the same name as the repository).
```python
    orders = client.create_repository("orders")
```
The client provides a method to look up all the Regions that have been created on the server already:
```python
    client.list_all_regions()
```

GemfireClient also has methods for querying and function execution which we will see later.

### Repository
--------------

Just like Spring's CrudRepository interface, the following methods are available on the Repository
```python
    save(entities)   #saves one or more entities in GemFire
    find(ids)        #finds entities with the given ids
    find_all()       #returns all data in region
    exists(id)       #checks to see if an entity with the given id exists
    delete(entities) #deletes the given entities from GemFire
    delete_all()     #deletes all data in the GemFire region
```

As the naming suggests, intention of these methods is pretty clear. One thing that needs to be highlighted here is that all entities need an identity; this library uses "id" instance variable as identity. So all entities that are stored in GemFire need to have an instance variable named "id".

### Region
----------

For advanced operations, we also provide access to Region, which defines the following methods:
```python
    create(key, value)  #will insert only if key does not exists
    update(key, value)  #will update only if the key exists
    keys()              # returns all keys in the region
    compare_and_set(key, oldvalue, newvalue) #sets the key to newvalue only if current value is equal ot oldvalue
```

### Querying
------------
GemfireClient provides API for running ad-hoc [OQL queries](http://gemfire.docs.pivotal.io/latest/userguide/index.html#developing/querying_basics/chapter_overview.html) on the server.
```python
    adhoc_query(query_string)  #OQL query string
```

For faster performance, you will want to run prepared OQL queries. GemfireClient provides the following APIs for this:
```python
    new_query(query_id, query_string) #registers and prepares the OQL query on the server
    run_query(query_id, query_args)   #runs the query with specified parameters 
```
