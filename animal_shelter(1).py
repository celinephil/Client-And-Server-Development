from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps
import os
import pprint

class AnimalShelter(object):
    """ CRUD operations for ANIMAL collection in MongoDB """
    
    def __init__(self, username, password):
        if username and password:
            # Initializing the MongoClient. Helps to access the MongoDB databases and collections.
            self.client = MongoClient('mongodb://%s:%s@localhost:55816' % (username, password))
        else:
            self.client = MongoClient('mongodb://localhost:55816')
        self.database = self.client['AAC']
    
    # Create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            data_create = self.database.animals.insert(data)  # Data should be dictionary.
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
    
    # Read method to implement the R in CRUD.
    def read_all(self, data):
        cursor = self.database.animals.find(data, {'_id':False} )
        return cursor
    
    def read(self, data): 
        if data is not None:
            data_read = self.database.animals.find_one(data)  # Returns a single document as a python dictionary.
            return data_read
        else:
            raise Exception("Nothing to save, because data parameter is empty")
    
    # Update method to implement the U in CRUD.
    def update(self, query, data):
        if data is not None:
            data_update = self.database.animals.update_one(query, data)
            return data_update 
        else: # Else MongoDB returned error message
            raise Exception("Nothing to update, because data parameter is empty")
    
    # Delete method to implement the D in CRUD.
    def delete(self, data):
        if data is not None:
            data_delete = self.database.animals.delete_one(data)
        else:# Else MongoDB returned error message
            raise Exception("Nothing to delete, because data parameter is empty")