from __future__ import annotations
from abc import ABC, abstractmethod

class DbFactory(ABC):
    #factory Method
    @abstractmethod
    def CreateConnector(ConnectionString): #DbConnector
        pass
    
    #generator of object
    def DataBase(OptionDbName) -> DbFactory:
        from DAO.SqliteFactory import SqliteFactory
        from DAO.MySQLdbFactory import MySQLdbFactory
        try:
            if OptionDbName == 'SQLite':
                return  SqliteFactory()
            elif OptionDbName  == 'MYSql':
                return MySQLdbFactory()
        except:
            print("Error!! O tipo de banco não consta nas opções fornecidas")
            