from __future__ import annotations
from DAO.DbConnector import DbConector
from DAO.MySQLdbConnector import MySQLdbConnector
from DAO.DbFactory import  DbFactory

class MySQLdbFactory(DbFactory):
    def CreateConnector(self, ConnectionString) -> DbConector:
        return MySQLdbConnector(ConnectionString)