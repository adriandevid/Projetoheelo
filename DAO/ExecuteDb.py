from __future__ import annotations
#Cliente
class ExecuteDb:
    def Execute() -> str:
        import DbFactory
        sqlite = DbFactory.DbFactory.DataBase('MYSql').CreateConnector('ola.db').Connect();

        return sqlite

        
if __name__ == '__main__':
    ExitFunctionStr = ExecuteDb.Execute()
    print(ExitFunctionStr)

