from pymongo import MongoClient

class DbConnection:
    def __init__(self,nombreBD,nombreColleccion):
        self.client = MongoClient('localhost', 27017)
        self.dbs = self.client[nombreBD][nombreColleccion]
