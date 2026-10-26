# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password):
        USER = username
        PASS = password
        HOST = 'localhost'
        PORT = 27017
        DB = 'aac'
        COL = 'animals'

        self.client = MongoClient(
            host=HOST,
            port=PORT,
            username=USER,
            password=PASS,
            authSource='admin'
        )
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

    # Create a method to return the next available record number for use in the create method
        # Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            try:
                self.database.animals.insert_one(data)
                return True
            except Exception as e:
                print("Error inserting document:", e)
                return False
        else:
            return False

    # Create method to implement the R in CRUD.
    def read(self, query):
        if query is not None:
            return list(self.database.animals.find(query))
        else:
            raise Exception("Nothing to read, because query parameter is empty")
            
    # Update method to implement the U in CRUD.
    def update(self, query, new_values):
        if query is not None:
            try:
                result = self.database.animals.update_many(
                    query,
                    {"$set": new_values}
                )
                return result.modified_count
            except Exception as e:
                print("Error updating document:", e)
                return 0
        else:
            raise Exception("Nothing to update, because query parameter is empty")

    # Delete method to implement the D in CRUD.
    def delete(self, query):
        if query is not None:
            try:
                result = self.database.animals.delete_many(query)
                return result.deleted_count
            except Exception as e:
                print("Error deleting document:", e)
                return 0
        else:
            raise Exception("Nothing to delete, because query parameter is empty")
