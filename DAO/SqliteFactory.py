from DbFactory import DbFactory
from SqliteConnector import SqliteConnector

class SqliteFactory(DbFactory):
    #Concrete Factory
    def CreateConnector(self, ConnectionString): 
        return SqliteConnector(ConnectionString)