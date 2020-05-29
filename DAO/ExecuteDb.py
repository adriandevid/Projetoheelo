from __future__ import annotations
#Cliente
class ExecuteDb:
    def Execute() -> str:
        import DbFactory
        sqlite = DbFactory.DbFactory.DataBase('SQLite').CreateConnector('ola.db').Connect();
        cursor = sqlite.cursor()

        return "banco conectado"

        
if __name__ == '__main__':
    ExitFunctionStr = ExecuteDb.Execute()
    print(ExitFunctionStr)

