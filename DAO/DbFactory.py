from __future__ import annotations
from abc import ABC, abstractmethod

class DbFactory(ABC):
    #factory Method
    @abstractmethod
    def CreateConnector(ConnectionString): #DbConnector
        pass
    
    #generator of object
    def DataBase(OptionDbName) -> DbFactory:
        from DAO.MySQLdbFactory import MySQLdbFactory
        try:
            if OptionDbName  == 'MYSql':
                return MySQLdbFactory()
        except:
            print("Error!! O tipo de banco não consta nas opções fornecidas")
            