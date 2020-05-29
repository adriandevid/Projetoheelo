from __future__ import annotations
from abc import ABC, abstractmethod

class DbFactory(ABC):
    #factory Method
    @abstractmethod
    def CreateConnector(ConnectionString): #DbConnector
        pass
    
    #generator of object
    def DataBase(OptionDbName) -> DbFactory:
        from SqliteFactory import SqliteFactory
        try:
            if OptionDbName == 'SQLite':
                return  SqliteFactory()
            elif OptionDbName  == 'MYSql':
                print("criou banco sqlserver!!")
            else:
                print("false")
        except:
            print("Error!! O tipo de banco não consta nas opções fornecidas")
            