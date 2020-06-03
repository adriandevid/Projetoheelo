from DbConnector import DbConector
import pymysql

class MySQLdbConnector(DbConector):
    def __init__(self, ConnectionString):
        super().__init__(ConnectionString)
    def Connect(self):
        ListOfConnection = self.ConnectionString.split(',')
        return pymysql.connect(ListOfConnection[0],ListOfConnection[1],ListOfConnection[2], ListOfConnection[3])