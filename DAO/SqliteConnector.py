from DAO.DbConnector import DbConector
import sqlite3

#product concret
class SqliteConnector(DbConector):
    def __init__(self, ConnectionString):
        super().__init__(ConnectionString)
    def Connect(self):
        return sqlite3.connect(self.ConnectionString)
        