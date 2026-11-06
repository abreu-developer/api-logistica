from pymongo import mongo_client



class MongoDbConnection:
    def __init__(self):
        self.__uri = None
        self.__client = None
        self.__conn = None      
        
    def connect(self):
        self.__client = self.__uri
        self.__conn = self.__client        
        
    def get_connection(self):
        return self.__conn
    
    
    
mongo_db_connection = MongoDbConnection()