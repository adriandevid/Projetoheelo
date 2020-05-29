
class DbFactury():
    #factory Method
    def CreateConnector(ConnectionString): #DbConnector
        pass
    
    def DataBase(OptionDbName):
        from SqliteFactury import SqliteFatcury
        try:
            if OptionDbName == 'SQLite':
                return  SqliteFatcury()
            elif OptionDbName  == 'MYSql':
                print("criou banco sqlserver!!")
            else:
                print("false")
        except:
            print("Error!! O tipo de banco não consta nas opções fornecidas")
            