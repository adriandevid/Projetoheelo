from DAO.DbFactory import DbFactory
from DAO.SqliteConnector import SqliteConnector

class SqliteFactory(DbFactory):
    #Concrete Factory
    def CreateConnector(self, ConnectionString): 
        return SqliteConnector(ConnectionString)