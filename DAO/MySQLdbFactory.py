from __future__ import annotations
from DbConnector import DbConector
from MySQLdbConnector import MySQLdbConnector
from DbFactory import  DbFactory

class MySQLdbFactory(DbFactory):
    def CreateConnector(self, ConnectionString) -> DbConector:
        return MySQLdbConnector(ConnectionString)