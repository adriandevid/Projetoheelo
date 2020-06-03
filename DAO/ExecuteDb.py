from __future__ import annotations
import mysql.connector
from mysql.connector import errorcode

#Cliente
class ExecuteDb:
    def Execute():
        import DbFactory
        #ConnectionString deve ser passada sem espaços entre cada virgula seguindo o esquema ("host,usuario,senha,bancodedados")
        sqlite = DbFactory.DbFactory.DataBase('MYSql').CreateConnector("localhost,root,,mydb").Connect();
        cursor1 = sqlite.cursor()
        cursor1.execute("SELECT * FROM tbcampus")
        sqlite.close()
        for i in cursor1:
            print(i)
        
if __name__ == '__main__':
    ExecuteDb.Execute()

