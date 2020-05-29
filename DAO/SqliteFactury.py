from DbFactury import DbFactury
from SqliteConnector import SqliteConnector
class SqliteFatcury(DbFactury):
    def CreateConnector(self, ConnectionString): 
        return SqliteConnector(ConnectionString)